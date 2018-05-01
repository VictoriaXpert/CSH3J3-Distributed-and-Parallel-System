#!/usr/bin/env python
#coding=utf8
"""
====================================
:mod: 테스트용 blocking XML-RPC 서버
====================================
.. moduleauthor:: 채문창 <mcchae@gmail.com>
.. note:: GNU

설명
=====

테스트용 blocking XML-RPC 서버
"""

##########################################################################################
import time
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

##########################################################################################
class TestSvc(object):
	def ping(self, pid, _sleep=0):
		for i in xrange(_sleep):
			print "[%d] %d" % (pid, i)
			time.sleep(1)
		return True

##########################################################################################
def doSvc():
	mgr = TestSvc()
	class RequestHandler(SimpleXMLRPCRequestHandler):
		rpc_paths = ('/TestSvc')
	server = SimpleXMLRPCServer(('0.0.0.0', 9000),
	                            requestHandler=RequestHandler,
	                            logRequests=False,
	                            allow_none=True,
	)
	server.register_introspection_functions()
	server.register_instance(mgr)
	server.serve_forever()

##########################################################################################
if __name__=='__main__':
	doSvc()
