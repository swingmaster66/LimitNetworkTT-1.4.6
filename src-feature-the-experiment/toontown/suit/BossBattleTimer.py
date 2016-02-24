from time import time
from direct.interval.IntervalGlobal import Func, Sequence, Track, LerpScaleInterval
from direct.task import Task
from panda3d.core import TextNode
from toontown.toonbase.ToontownGlobals import getSuitFont

TEXT_GREEN = (0.0, 1.0, 0.0, 1.0)
TEXT_WHITE = (1.0, 1.0, 1.0, 1.0)


class BossBattleTimer:
    def __init__(self):
        self.text = None
        self.textNodePath = None
        self.flashTrack = None
        self.textSequence = None
        self.startTime = 0
        self.endTime = 0

    def load(self):
        self.text = TextNode('BossBattleTimer')
        self.text.setAlign(TextNode.ACenter)
        self.text.setFlattenFlags(TextNode.FFMedium)
        self.text.setFont(getSuitFont())
        self.text.setTextScale(0.075)
        self.text.setTextColor(*TEXT_WHITE)
        self.textNodePath = aspect2d.attachNewNode(self.text)
        self.textNodePath.reparentTo(base.a2dBottomLeft)
        self.textNodePath.setPos(0.60, 0.0, 0.15)

    def makeFlashTrack(self):
        return Track(
            (0.25, Func(self.text.setTextColor, *TEXT_GREEN)),
            (0.50, Func(self.text.setTextColor, *TEXT_WHITE)),
            (0.75, Func(self.text.setTextColor, *TEXT_GREEN)),
            (1.0, Func(self.text.setTextColor, *TEXT_WHITE)),
            (1.25, Func(self.text.setTextColor, *TEXT_GREEN)),
            (1.50, Func(self.text.setTextColor, *TEXT_WHITE)),
            (1.75, Func(self.text.setTextColor, *TEXT_GREEN)),
            (2.0, Func(self.text.setTextColor, *TEXT_WHITE)),
        )

    def makeGrowShrinkSequence(self):
        return Sequence(
            LerpScaleInterval(self.textNodePath, duration=2.0, scale=1.1, startScale=0.9),
            LerpScaleInterval(self.textNodePath, duration=2.0, scale=0.9, startScale=1.1),
        )

    def destroy(self):
        if self.flashTrack:
            self.flashTrack.finish()
            self.flashTrack = None
        if self.textSequence:
            self.textSequence.finish()
            self.textSequence = None
        if self.text:
            self.text.setText('')
        if self.textNodePath:
            self.textNodePath.removeNode()

    def start(self, startTime):
        self.startTime = startTime
        self.endTime = 0
        if self.textNodePath:
            taskMgr.doMethodLater(0.05, self.updateText, 'updateBossText-%s' % self.startTime)
            self.textSequence = self.makeGrowShrinkSequence()
            self.textSequence.loop()

    def updateText(self, task=None):
        self.text.setText(str(round(time() - self.startTime, 3)) + ' seconds')
        if self.endTime != 0:
            return Task.done
        return Task.again

    def stop(self, endTime):
        self.endTime = endTime
        taskMgr.remove('updateBossText-%s' % self.startTime)
        if self.textNodePath:
            self.text.setText(str(round(self.endTime - self.startTime, 3)) + ' seconds')
            self.flashTrack = self.makeFlashTrack()
            self.flashTrack.start()
