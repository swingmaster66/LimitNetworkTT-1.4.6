from direct.showbase.DirectObject import DirectObject


class Ouch(DirectObject):
    def __init__(self, keyEvent, callback):
        DirectObject.__init__(self)

        self.accept(keyEvent, callback)

    def destroy(self):
        self.ignoreAll()


class CyclePlacer(DirectObject):
    def __init__(self, locations, keyEvent, startIndex=0):
        DirectObject.__init__(self)

        self.locations = locations
        self.index = startIndex
        self.accept(keyEvent, self.gotoNextLocation)

    def destroy(self):
        self.locations = None
        self.ignoreAll()

    def gotoNextLocation(self):
        self.index = (self.index + 1) % len(self.locations)
        self.gotoLocation()

    def gotoLocation(self, index=None):
        if index is None:
            index = self.index

        pos, h = self.locations[index]
        base.localAvatar.reparentTo(render)
        base.localAvatar.setPos(*pos)
        base.localAvatar.setH(h)


class ToonLifter(DirectObject):
    SerialNum = 0

    def __init__(self, keyDownEvent, speed=2):
        DirectObject.__init__(self)

        self.serialNum = ToonLifter.SerialNum
        ToonLifter.SerialNum += 1
        self.taskName = 'ToonLifter%s' % self.serialNum
        self.keyDownEvent = keyDownEvent
        self.keyUpEvent = self.keyDownEvent + '-up'
        self.speed = speed
        self.accept(self.keyDownEvent, self.startLifting)

    def destroy(self):
        self.ignoreAll()
        taskMgr.remove(self.taskName)

    def startLifting(self):

        def liftTask(task, self=self):
            base.localAvatar.setZ(base.localAvatar.getZ() + self.speed)
            return task.cont

        def stopLifting(self=self):
            taskMgr.remove(self.taskName)
            self.ignore(self.keyUpEvent)
            self.accept(self.keyDownEvent, self.startLifting)

        self.ignore(self.keyDownEvent)
        self.accept(self.keyUpEvent, stopLifting)
        taskMgr.add(liftTask, self.taskName)
