from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


def file_download():  # membuat fungsi download
    # membuka file berupa .jpg yang dikirimkan server
    handle = open("aditya alif nugraha-foto.jpg", 'rb')
    # Mengambalikan hasil dalam bentuk biner
    return xmlrpc.client.Binary(handle.read())
    handle.close()  # menutup koneksi host


# membuat objek dari kelas SimpleXMLRPCServer dengan menggunakan IP server
server = SimpleXMLRPCServer(('10.20.3.242', 8000))


def adder_function(x, y):
    return x + y


server.register_function(adder_function, 'add')

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'mul').
print("Listening on port 8000")  # menampilkan pesan jika sudah terjadi koneksi

# mendaftarkan fungsi yang dapat digunakan oleh client
server.register_function(file_download, 'download')

server.serve_forever()  # server akan terus menyala sampai PC dimatikan
