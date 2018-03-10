import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://10.20.3.242:8000")
with open("foto.jpg",'rb') as handle:
    data = xmlrpc.client.Binary(handle.read())
    handle.close()
    result = proxy.file_upload(data)