from pandac.PandaModules import *

def makeCard(book=False):
    cardMaker = CardMaker('papyrus-cm')
    cardMaker.setHasUvs(1)
    cardMaker.setFrame(-0.5, 0.5, -0.5, 0.5)

    nodePath = NodePath('papyrus')
    nodePath.setBillboardPointEye()

    phBase = nodePath.attachNewNode(cardMaker.generate())
    phBase.setTexture(loader.loadTexture('phase_3/maps/papyrus_head.rgba'))
    phBase.setY(-0.3)
    phBase.setTransparency(True)

    phFace = nodePath.attachNewNode(cardMaker.generate())
    phFace.setTexture(loader.loadTexture('phase_3/maps/papyrus_head.rgba'))
    phFace.setY(-0.302)
    phFace.setTransparency(True)

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
