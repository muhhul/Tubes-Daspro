def help (user):
    if user[1]=='' : #belum login
        print("================ HELP ================", end="\n")
        print("1. login \n   Untuk masuk menggunakan akun")
        print ("2. exit \n   Untuk keluar dari program dan kembali ke terminal")
    else:
        if user[1] == 'bandung_bondowoso': #user merupakan bandung bondowoso
            print("================ HELP ================", end="\n")
            print ("1. logout \n   Untuk keluar dari akun yang digunakan sekarang")
            print ("2. summonjin \n   Untuk memanggil jin")
            print ("3. hapusjin \n   Untuk menghapus jin")
            print ("4. ubahjin \n   Untuk mengubah tipe jin dengan tipe jin yang tersedia adalah Jin Pengumpul dan Jin Pembangun")
            print ("5. batchkumpul \n   Untuk mengerahkan seluruh jin pengumpul untuk mengumpulkan resource candi")
            print ("6. batchbangun \n   Untuk mengerahkan seluruh jin pembangun untuk membangun candi")
            print ("7. laporanjin \n   Untuk mengambil laporan jin")
            print ("8. laporancandi \n   Untuk mengambil laporan candi")
            print ("9. save \n   Untuk menyimpan data")
            print ("10. exit \n   Untuk keluar dari program dan kembali ke terminal")
        elif user[1] == 'roro_jonggrang': # user merupakan roro jonggrang
            print("================ HELP ================", end="\n")
            print ("1. logout \n   Untuk keluar dari akun yang digunakan sekarang")
            print ("2. hancurkancandi \n   Untuk menghancurkan candi yang telah dibangun oleh Bandung Bondowoso")
            print ("3. ayamberkokok \n   Untuk menyelesaikan permainan dengan memalsukan pagi hari")
            print ("4. save \n   Untuk menyimpan data")
            print ("5. exit \n   Untuk keluar dari program dan kembali ke terminal")
        elif user[1]== 'pengumpul': # user merupakan jin pengumpul
            print("================ HELP ================", end="\n")
            print ("1. logout \n   Untuk keluar dari akun yang digunakan sekarang")
            print ("2. kumpul \n   Untuk mengumpulkan resource candi")
            print ("3. save \n   Untuk menyimpan data")
            print ("4. exit \n   Untuk keluar dari program dan kembali ke terminal")
        elif user[1]== 'pembangun': #user merupakan jin pembangun
            print("================ HELP ================", end="\n")
            print ("1. logout \n   Untuk keluar dari akun yang digunakan sekarang")
            print ("2. bangun \n   Untuk membangun candi")
            print ("3. save \n   Untuk menyimpan data")
            print ("4. exit \n   Untuk keluar dari program dan kembali ke terminal")
            