from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def file_download():#membuat fungsi download
    handle = open("aditya alif nugraha-foto.jpg",'rb')#membuka file berupa .jpg yang dikirimkan server
    return xmlrpc.client.Binary(handle.read())#Mengambalikan hasil dalam bentuk biner
    handle.close()#menutup koneksi host

server = SimpleXMLRPCServer(('10.20.3.242',8000))#membuat objek dari kelas SimpleXMLRPCServer dengan menggunakan IP server
def adder_function(x,y):
        return x + y
    server.register_function(adder_function, 'add')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
print ("Listening on port 8000")#menampilkan pesan jika sudah terjadi koneksi

server.register_function(file_download,'download')#mendaftarkan fungsi yang dapat digunakan oleh client

server.serve_forever()#server akan terus menyala sampai PC dimatikan