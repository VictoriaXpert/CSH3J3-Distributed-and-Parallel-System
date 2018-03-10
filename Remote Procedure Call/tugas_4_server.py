from xmlrpc.server import SimpleXMLRPCServer 
import xmlrpc.client 

 
def file_download(): 
    handle = open("Aditya Alif Nugraha - Photo.jpg", 'rb') 
    return xmlrpc.client.Binary(handle.read()) 
    handle.close() 

 
# membuat fungsi file upload dengan parameter file data yang akan dikirim dari client 
def file_upload(filedata): 
    # menentukan tempat untuk menyimpan file yang diupload dari client 
    with open("uploaded file.jpg", 'wb') as handle: 
        data1 = filedata.data  # convert from byte to binary IMPORTANT! 
        handle.write(data1)  # menulis data yang diupload dari client 
        handle.close()  # menutup file yang telah ditulis 
        return True  # IMPORTANT 
# must have return value 
# else error messsage: "cannot marshal None unless allow_none is enabled" 

 
server = SimpleXMLRPCServer(('10.20.3.242', 8000)) 
print("Listening on port 8000") 
server.register_introspection_functions() 
server.register_function(file_download, 'download') 
# mendaftarkan fungsi yang dapat digunakan oleh client 
server.register_function(file_upload, 'file_upload') 

 
server.serve_forever()