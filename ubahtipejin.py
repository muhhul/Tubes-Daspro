def UbahTipeJin ():
    jin = input("Masukkan username jin: ")
    if jin == ketemu: #ketemu di data
        tipe = tipejin #tipe yang tertera di csv
        if tipejin == 'pembangun': #jin pembangun
            print("Jika ini bertipe pembangun. Yakin ingin mengubah ke tipe pengumpul")
            pilihan = input("(Y/N)? ")
            if pilihan == 'Y': 
                print ("Jin telah berhasil diubah.")
            else:
                print ("Pengubahan jin dibatalkan.")
        else: #jin pengumpul
            print("Jika ini bertipe pembangun. Yakin ingin mengubah ke tipe pengumpul")
            pilihan = input("(Y/N)? ")
            if pilihan == 'Y': 
                print ("Jin telah berhasil diubah.")
            else:
                print ("Pengubahan jin dibatalkan.")
    else: 
        print ("Tidak ada jin dengan username tersebut")
