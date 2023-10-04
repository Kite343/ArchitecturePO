import zope.interface

class IModelChanger(zope.interface.Interface):

    def notify_change(self, sender):
        pass