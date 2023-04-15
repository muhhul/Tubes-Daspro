import argparse
import sys
import os
import function
import time

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

