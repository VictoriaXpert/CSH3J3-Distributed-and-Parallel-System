import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://10.20.3.242:8000')
#print(s.pow(2,3))  # Returns 2**3 = 8
#print(s.add(2,3))  # Returns 5
#print(s.mul(5,2))  # Returns 5*2 = 10

# Print list of available methods
print(s.system.listMethods())
#s.add(1,2)
#print(s.add(1,2))
#print(s.sum([5,7,5,0,9,1,4]))