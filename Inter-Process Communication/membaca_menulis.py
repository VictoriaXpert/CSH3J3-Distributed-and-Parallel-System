### Membaca file
# membuka file bernama "test.txt"
# menentukan operasinya yaitu membaca "r"
# b adalah byte, memperlakukan file sebagai byte
# tanpa b hanya dapat menulis text ("ASCII")

handle = open("test.txt","r")   #sebagai text biasa
#handle = open("test.txt","rb") # sebagai byte

data = handle.read(2) #membaca 2 byte

while data != '': # End of file untuk text
#while data != b'': #End of File untuk byte
    #lakukan sesuatu misalkan print
    print (data)
    data = handle.read(2) # membaca 2 byte selanjutnya

handle.close() # selalu tutup file jika sudah selesai digunakan

###Menulis File
PESAN = "hello world!"
handle = open("hasil_tulis.txt","w")   #sebagai text biasa
handle.write(PESAN)
handle.close()