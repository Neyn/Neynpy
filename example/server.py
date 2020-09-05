from neynpy.core.server import Server
from neynpy.core.route import Router
from neynpy.http.response import Response


def about(request):
    return Response('return from about view', 200)


def main(request):
    print(request.method, request.path)
    return Response('hello from NeynPy')


router = Router()
router.add_handler('/', main)
router.add_handler('/about', about)

_server = Server(ip='127.0.0.1', port='9090', router=router)
_server.run()
