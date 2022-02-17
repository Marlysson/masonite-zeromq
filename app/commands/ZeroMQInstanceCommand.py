from masonite.commands import Command


class ZeroMQInstanceCommand(Command):
    """
    Start a zeromq instance

    zeromq:serve
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def handle(self):
        self.info("Started !")

        import zmq

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5555")

        while True:
            message = socket.recv()
            print("Received request: %s" % message)
            socket.send(b"OK")
