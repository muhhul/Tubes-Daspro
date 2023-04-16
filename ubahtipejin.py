def UbahTipeJin ():
    jin = input("Masukkan username jin: ")
    if jin == ketemu: #ketemu di data
        print("Jika ini bertipe "...". Yakin ingin mengubah ke tipe "...")")
        pilihan = input("(Y/N)? ")
        if pilihan == 'Y': 
            print ("Jin telah berhasil diubah.")
        else:
            print ("Pengubahan jin dibatalkan.")
    else: 
        print ("Tidak ada jin dengan username tersebut")