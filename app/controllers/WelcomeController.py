"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from masonite.request import Request

class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View, request: Request):
        
        import zmq

        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")

        data = request.input("data").encode("utf-8")
        socket.send(bytes(data))
        
        message = socket.recv()
        print("Received reply %s [ %s ]" % (data, message))

        return view.render("welcome")
