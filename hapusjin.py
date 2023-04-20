import function
import hancurkancandi

def hapusjin (listUser,listCandi):
    jin = input("Masukkan username jin: ")
    for i in range(function.newLen(listUser)):
        if jin == listUser[i][0]:
            print(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)?")
            choice = input("(Y/N)?")
            if choice == 'Y':
                print("Jin telah berhasil dihapus dari alam gaib.")
                listUser[i][0]='0'
                hancurkancandi.hancurkancandi(listCandi)
            else:
                print("Jin batal dihapus.")
            break
        elif i+1 == function.newLen(listUser):
            print("Tidak ada jin dengan username tersebut.")