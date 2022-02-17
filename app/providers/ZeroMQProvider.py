from masonite.providers import Provider
from app.commands.ZeroMQInstanceCommand import ZeroMQInstanceCommand

class ZeroMQProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.make("commands").add(ZeroMQInstanceCommand(self.application))

    def boot(self):
        pass
