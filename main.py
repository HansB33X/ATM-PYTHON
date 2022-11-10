import os
import json
import time
from tqdm import tqdm

def loading():
    for i in tqdm(range(100)):
        time.sleep(0.1)

def login():
    UserName = input("Masukan Username> ")
    PIN = input("Masukan PIN> ")
    with open('data.json', 'r') as data:
        if UserName and PIN in data.read():
            print("Membaca Data...")
            loading()
            time.sleep(1)
            print("Berhasil mendapatkan data...")
            time.sleep(1)
            os.system("clear")
            main()

        else:
            print("Maaf data yang anda masukan tidak ada")
            newUser = input("Apakah anda pengguna baru? [Y/N]\n>")
            if newUser == "Y":
                os.system("python3 newUser.py")
            elif newUser == "N":
                login()
            else:
                print("Mohon masukan keterangan Y/N")
                time.sleep(1)
                os.system("clear")
                login()



def tarikTunai(Saldo, nominal):
    return Saldo - nominal

def transfer(Saldo, nominal):
    return Saldo - nominal

def main():
    Saldo = int(1000000000)
    pilihanMenu = int(input("="*20 + "\n" + "\tMENU\n" + "="*20 + "\n" + "1.) Tarik Tunai              2.) Transfer\n>"))
    if pilihanMenu == 1:
        nominal = int(input("Masukan Nominal> "))
        print(tarikTunai(Saldo, nominal))
    elif pilihanMenu == 2:
        nominal = int(input("Masukan Nominal> "))
        print(transfer(Saldo, nominal))
    else:
        print("Pilihan yang anda masukan tidak ada...")
        main()


if __name__ == '__main__':
    login()