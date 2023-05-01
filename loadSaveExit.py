import argparse
import sys
import os
import function
import time
import shutil

path = r"C:\Users\Ardra Rafif S\Documents\ITB\TPB\Semester 2\Daspro\Tubes new\Tubes-Daspro\FileLoad" #program akan error
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

fileUser.close()
fileCandi.close()
fileBahan.close()

def write(list,arrFile,x):
    file= open(f"{arrFile}","w")
    for i in range(function.newLen(list)):
        for j in range(x):
            if list[i][0]!='0':
                if j == x-1:
                    file.write(str(list[i][j]))
                    file.write("\n")
                else:
                    file.write(str(list[i][j]))
                    file.write(";")
    file.close()

def save():
    os.chdir(r"C:\Users\Ardra Rafif S\Documents\ITB\TPB\Semester 2\Daspro\Tubes new\Tubes-Daspro") #ganti sesuai dengan penyipanan directory kamu
    arrFolder=os.listdir()
    cekFolder2 = function.mencari(arrFolder,'FileLoad')
    os.chdir(path)
    arrFolder=os.listdir()
    saveFolder = input("Masukkan nama folder: ")
    cekFolder1 = function.mencari(arrFolder,saveFolder)
    if cekFolder1==True and cekFolder2==True:
        newPath = f"{path}\{saveFolder}"
        os.chdir(newPath)
        arrFile = os.listdir()
        write(listUser,arrFile[2],3)
        write(listCandi,arrFile[1],5)
        write(listBahan,arrFile[0],3)

        print("")
        print("Saving...")
        time.sleep(1.5)
        print("")
        print(f"Berhasil menyimpan data di folder FileLoad/{saveFolder}!")
    elif cekFolder2==True:
        shutil.copytree('newgame',f'{saveFolder}')
        newPath = f"{path}\{saveFolder}"
        os.chdir(newPath)
        arrFile = os.listdir()
        write(listUser,arrFile[2],3)
        write(listCandi,arrFile[1],5)
        write(listBahan,arrFile[0],3)

        print("")
        print("Saving...")
        time.sleep(1.5)
        print("")
        print(f"Memuat folder FileLoad/{saveFolder}...")
        time.sleep(1.5)
        print("")
        print(f"Berhasil menyimpan data di folder FileLoad/{saveFolder}!")
    else:
        os.chdir(r"C:\Users\Ardra Rafif S\Documents\ITB\TPB\Semester 2\Daspro\Tubes new\Tubes-Daspro") #ganti sesuai dengan penyipanan directory kamu
        os.makedirs('/FileLoad')
        os.chdir(path)
        shutil.copytree('TemplateLoad',f'{saveFolder}')
        newPath = f"{path}\{saveFolder}"
        os.chdir(newPath)
        arrFile = os.listdir()
        write(listUser,arrFile[2],3)
        write(listCandi,arrFile[1],5)
        write(listBahan,arrFile[0],3)

        print("")
        print("Saving...")

def exit():
    inputUser = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N)")
    while (inputUser != 'Y' and inputUser != 'N'):
        inputUser = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N)")
    if inputUser == 'Y':
        save()
        sys.exit()
    elif inputUser == 'N':
        sys.exit()
    else:
        exit()