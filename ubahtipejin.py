import function

def UbahTipeJin (listUser,user):
    if user=='bandung_bondowoso':
        jin = input("Masukkan username jin: ")
        for i in range(function.newLen(listUser)):
            if jin == listUser[i][0]: #ketemu di data
                tipe = listUser[i][2] #tipe yang tertera di csv
                if tipe == 'pembangun': #jin pembangun
                    print("Jika ini bertipe pembangun. Yakin ingin mengubah ke tipe pengumpul")
                    pilihan = input("(Y/N)? ")
                    if pilihan == 'Y': 
                        listUser[i][2]='pengumpul'
                        print ("Jin telah berhasil diubah.")
                    else:
                        print ("Pengubahan jin dibatalkan.")
                else: #jin pengumpul
                    print("Jika ini bertipe pengumpul. Yakin ingin mengubah ke tipe pembangun")
                    pilihan = input("(Y/N)? ")
                    if pilihan == 'Y': 
                        listUser[i][2]='pembangun'
                        print ("Jin telah berhasil diubah.")
                    else:
                        print ("Pengubahan jin dibatalkan.")
                break
            elif i+1 == function.newLen(listUser): 
                print ("Tidak ada jin dengan username tersebut")
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")
