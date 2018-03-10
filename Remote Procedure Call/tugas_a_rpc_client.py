import xmlrpc
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://10.20.3.242:8000')#untuk mengenali IP dari server yang dituju
handle = open("foto.jpg","wb")#untuk membaca file berupa .txt
handle.write(proxy.download().data)#untuk menuliskan file yang diterima dari server
handle.close()#menutup koneksi host

