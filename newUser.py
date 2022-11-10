import json
import os
import time

def Registrasi(new_data, filename='data.json'):
    with open(filename,'r+') as file:
        fileData = json.load(file)
        fileData["users"].append(new_data)
        file.seek(0)
        json.dump(fileData, file, indent = 4)
        os.system("clear")
        print("Data berhasil ditambahkan\nSekarang Jalankan kembali main.py")
        time.sleep(1)   
 
namaUser = input("Masukan Nama> ")
jobUser = input("Pekerjaan> ")
pinUser = int(input("Masukan pin 6 digit> "))

data = {"Username":namaUser,
     "Job": jobUser,
     "PIN": pinUser
    }
     
Registrasi(data)