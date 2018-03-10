import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://10.20.3.242:8000')
handle = open("foto.jpg","wb")#untuk membaca file berupa .jpg
handle.write(s.download().data)#untuk menuliskan file yang diterima dari server
handle.close()#menutup koneksi host

# Print list of available methods
print(s.system.listMethods())
