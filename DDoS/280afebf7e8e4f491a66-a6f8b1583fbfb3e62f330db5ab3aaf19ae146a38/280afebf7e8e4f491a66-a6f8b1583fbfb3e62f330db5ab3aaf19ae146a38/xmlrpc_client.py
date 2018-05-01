#!/usr/bin/env python
#coding=utf8
import os
from xmlrpc.client import ServerProxy
proxy = ServerProxy("http://localhost:9000/TestSvc")
print("[%d] TestSvc.ping(5)=%s" % (os.getpid(), proxy.ping(os.getpid(), 5)))
