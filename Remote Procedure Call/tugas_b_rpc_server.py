from xmlrpc.server import SimpleXMLRPCServer


def file_upload(filedata):
    with open("uploaded_file.txt", 'wb') as handle:
        data1 = filedata.data  # convert from byte to binary IMPORTANT!
        handle.write(data1)
        handle.close()
        return True  # IMPORTANT
# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"


server = SimpleXMLRPCServer(('localhost', 8000))
print("Listening on port 8000")

server.register_function(file_upload, 'file_upload')

server.serve_forever()
