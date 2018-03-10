import socket               
 
s = socket.socket()         
print ("Socket berhasil dibuat")

ip = "192.168.43.135" 
port = 12345               

s.bind((ip, port))        
print ("socket bind ke %s" %(port))
 
s.listen(5)     
print ("socket mendengarkan")           
 
while True:
   c, addr = s.accept()     
   print ('Mendapat koneksi dari', addr) 
   c.send ("Terima kasih telah terkoneksi".encode())
   c.close()