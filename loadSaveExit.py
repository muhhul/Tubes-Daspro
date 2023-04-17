import argparse
import sys
import os
import function
import time
import shutil

path = r"D:\Hul\ITB\Akademik\Daspro\Tubes\FileLoad" #program akan error
# ganti alamat folder sesuai folder kamu
# path = r"..............\FileLoad" isi titik titk sesuai tempat penyimpanan
os.chdir(path)
arrFolder=os.listdir()

#def load():
parser = argparse.ArgumentParser(description='Masukkan Nama Folder')
parser.add_argument('namaFolder', type=str, nargs = '?', help='Nama Folder', default='')
args = parser.parse_args()

cekLoad = function.mencari(arrFolder,args.namaFolder)
if cekLoad==True:
    print("")
    print("Loading...")
    time.sleep(1.5)
    print("")
    print("Memuat data...")
    time.sleep(1.5)
    os.system('cls')
elif args.namaFolder=='':
    print("")
    print("Loading...")
    time.sleep(1.5)
    print("")
    print("Tidak ada nama folder yang diberikan!")
    sys.exit()
else:
    print("")
    print("Loading...")
    time.sleep(1.5)
    print("")
    print(f'Folder "{args.namaFolder}" tidak ditemukan.')
    sys.exit()

newPath = f"{path}\{args.namaFolder}"
os.chdir(newPath)
arrFile = os.listdir()

fileUser = open(f"{arrFile[2]}","r")
fileCandi = open(f"{arrFile[1]}","r")
fileBahan = open(f"{arrFile[0]}","r")

listUser = fileUser.readlines()
listCandi = fileCandi.readlines()
listBahan = fileBahan.readlines()

listUser = function.newSplit(listUser,3)
listCandi = function.newSplit(listCandi,5)
listBahan = function.newSplit(listBahan,3)

def user():
    return listUser
def candi():
    return listCandi
def bahan():
    return listBahan

def save():
    os.chdir(r"D:\Hul\ITB\Akademik\Daspro\Tubes")
    arrFolder=os.listdir()
    cekFolder2 = function.mencari(arrFolder,'FileLoad')
    os.chdir(path)
    arrFolder=os.listdir()
    saveFolder = input("Masukkan nama folder: ")
    cekFolder1 = function.mencari(arrFolder,saveFolder)
    if cekFolder1==True and cekFolder2==True:
        print("")
        print("Saving...")
        time.sleep(1.5)
        print("")
        print(f"Berhasil menyimpan data di folder FileLoad/{saveFolder}!")
    elif cekFolder2==True:
        shutil.copytree('TemplateLoad',f'{saveFolder}')
        print("")
        print("Saving...")
        time.sleep(1.5)
        print("")
        print(f"Memuat folder FileLoad/{saveFolder}...")
        time.sleep(1.5)
        print("")
        print(f"Berhasil menyimpan data di folder FileLoad/{saveFolder}!")
    else:
        print("")
        print("Saving...")

def exit():
    inputUser = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    while (inputUser != 'n' and inputUser != 'y'):
        inputUser = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if inputUser == 'y':
        save()