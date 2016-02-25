import random
from pandac.PandaModules import *

def makeCard(book=False):
    cardMaker = CardMaker('sans-cm')
    cardMaker.setHasUvs(1)
    cardMaker.setFrame(-0.5, 0.5, -0.5, 0.5)

    nodePath = NodePath('sans')
    nodePath.setBillboardPointEye()

    shBase = nodePath.attachNewNode(cardMaker.generate())
    shBase.setTexture(loader.loadTexture('phase_3/maps/sans_head.rgba'))
    shBase.setY(-0.3)
    shBase.setTransparency(True)

    shFace = nodePath.attachNewNode(cardMaker.generate())
    shFace.setTexture(loader.loadTexture('phase_3/maps/sans_head.rgba'))
    shFace.setY(-0.302)
    shFace.setTransparency(True)

    return nodePath


def addHeadEffect(head, book=False):
    card = makeCard(book=book)
    card.setScale(1.45 if book else 2.5)
    card.setZ(0.05 if book else 0.5)
    for nodePath in head.getChildren():
        nodePath.removeNode()
    card.instanceTo(head)


def addToonEffect(toon):
    toon.getDialogueArray = lambda *args, **kwargs: []
    for lod in toon.getLODNames():
        addHeadEffect(toon.getPart('head', lod))
