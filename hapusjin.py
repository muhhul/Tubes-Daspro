import function
import hancurkancandi

def hapusjin (listUser,listCandi,user):
    if user=='bandung_bondowoso':
        jin = input("Masukkan username jin: ")
        for i in range(function.newLen(listUser)):
            if jin == listUser[i][0]:
                print(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)?")
                choice = input("(Y/N)?")
                if choice == 'Y':
                    print("Jin telah berhasil dihapus dari alam gaib.")
                    listUser[i][0]='0'
                    hancurkancandi.hancurkancandi(listCandi,'roro_jonggrang')
                else:
                    print("Jin batal dihapus.")
                break
            elif i+1 == function.newLen(listUser):
                print("Tidak ada jin dengan username tersebut.")
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")