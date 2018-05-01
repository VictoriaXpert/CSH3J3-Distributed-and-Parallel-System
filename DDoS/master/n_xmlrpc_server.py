##########################################################################################
import time
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

##########################################################################################



##########################################################################################


def doSvc():
    mgr = TestSvc()
    from socketserver import ThreadingMixIn

    class SimpleThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
        pass

    class RequestHandler(SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC2')

    server = SimpleThreadXMLRPCServer(('192.168.1.5', 8000),
                                      requestHandler=RequestHandler,
                                      logRequests=False,
                                      allow_none=True,
                                      )
    server.register_introspection_functions()
    server.register_instance(mgr)
    server.serve_forever()


##########################################################################################
if __name__ == '__main__':
    doSvc()
