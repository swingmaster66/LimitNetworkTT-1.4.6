from panda3d.core import Loader, LoaderOptions, Filename, NodePath

from direct.showbase.DirectObject import DirectObject
from direct.directnotify.DirectNotifyGlobal import directNotify


class Preloader(DirectObject):
    notify = directNotify.newCategory('Preloader')

    def __init__(self):
        DirectObject.__init__(self)

        self.loader = Loader.getGlobalPtr()

        self.modelPool = {}

        self.requests = {}

        self.asyncRequestDoneEvent = self.getUniqueName() + '-asyncRequestDone'
        self.accept(self.asyncRequestDoneEvent, self.__handleAsyncRequestDone)

    def destroy(self):
        self.ignore(self.asyncRequestDoneEvent)

        for key in self.requests.keys():
            self.cancelAsyncRequest(key)

        for key in self.modelPool.keys():
            self.unloadModel(key)

    def getUniqueName(self):
        return 'Preloader-' + str(id(self))

    def loadModel(self, modelPath, priority=None):
        self.notify.debug('Loading model... ' + modelPath)

        request = self.loader.makeAsyncRequest(
            Filename(modelPath),
            LoaderOptions(LoaderOptions.LFSearch |
                          LoaderOptions.LFReportErrors |
                          LoaderOptions.LFNoCache))
        if priority is not None:
            request.setPriority(priority)
        request.setDoneEvent(self.asyncRequestDoneEvent)
        request.setPythonObject(modelPath)
        self.requests[modelPath] = (
            request, self.loadModelCallback, [modelPath])

        self.loader.loadAsync(request)

    def loadModelCallback(self, nodePath, modelPath):
        if nodePath is None:
            return

        gsg = base.win.getGsg()
        if gsg:
            nodePath.prepareScene(gsg)

        self.modelPool[modelPath] = nodePath

    def unloadModel(self, modelPath):
        self.notify.debug('Unloading model... ' + modelPath)

        if modelPath in self.requests:
            self.cancelAsyncRequest(modelPath)

        nodePath = self.modelPool.pop(modelPath, None)
        if nodePath is not None:
            nodePath.removeNode()

    def getModel(self, modelPath):
        return self.modelPool.get(modelPath)

    def cancelAsyncRequest(self, key):
        request = self.requests.pop(key, (None,))[0]
        if request is not None:
            self.loader.remove(request)

    def __handleAsyncRequestDone(self, request):
        key = request.getPythonObject()

        if key not in self.requests:
            return

        request, callback, extraArgs = self.requests.pop(key)

        obj = None

        if hasattr(request, 'getModel'):
            node = request.getModel()
            if node is not None:
                obj = NodePath(node)

        callback(obj, *extraArgs)
