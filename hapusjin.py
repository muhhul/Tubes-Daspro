import function
import hancurkancandi

def hapusjin (listUser,listCandi,user,listJin):
    if user=='bandung_bondowoso':
        jin = input("Masukkan username jin: ")
        for i in range(2,function.newLen(listUser)):
            if jin == listUser[i][0] and i!=2:
                print(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)?")
                choice = input("(Y/N)?")
                if choice == 'Y':
                    print("Jin telah berhasil dihapus dari alam gaib.")
                    listUser[i][0]='0'
                    for i in range(function.newLen(listCandi)):
                        if listCandi[i][1]==jin:
                            listCandi[i][0]='0'
                    for i in range(function.newLen(listJin)):
                        if listJin[i][0]==jin:
                            listJin[i][0]='0'
                else:
                    print("Jin batal dihapus.")
                break
            elif i+1 == function.newLen(listUser):
                print("Tidak ada jin dengan username tersebut.")
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")