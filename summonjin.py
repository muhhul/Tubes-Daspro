def summonjin():
    # cek user bondowoso atau bkn?
    if logged_user[0] != "Bondowoso":
        print("summon jin gagal")
        return
    
    
    
    # cek apakah jin sudah penuh atau belum
    with open("./FileLoad/Load1/user.csv") as f:
        rows = f.read().splitlines()
        # Loop CSV
        count = 0
        for i in range(newLen(rows)):
            row = rows[i]
            # TODO: Aldi: NewSplit bermasalah, sampai dibenarkan, akan memakai split
            [ctx_username, ctx_password, ctx_role] = row.split(";")
            if i == 0:
                continue
            if ctx_role == "jin_pengumpul" or ctx_role == "jin_pembangun":
                count += 1

        if count > 100:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            return
        # jika iya (summon jenis jin)
        print("Jenis jin yang dapat dipanggil: (1) Pengumpul - Bertugas mengumpulkan bahan bangunan(2) Pembangun - Bertugas membangun candi")
        
        role_jin_pengumpul = 1
        role_jin_pembangun = 2
        # jika tidak input jenis lagi
        while True:
            input_role = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            if input_role == role_jin_pengumpul:
                print("Memilih jin \"Pengumpul\"")
                break
            if input_role == role_jin_pembangun:
                print("Memilih jin \"pembangun\"")
                break
            print(f"Tidak ada jenis jin bernomor \"{input_role}\"!")
        # jika iya pilih jin dan masukan nama user
          
        for i in range(newLen(rows)):
            row = rows[i]
            if i == 0:
                continue
            # TODO: Aldi: NewSplit bermasalah, sampai dibenarkan, akan memakai split
            [ctx_username, ctx_password, ctx_role] = row.split(";")

        # cek nama user sudah dipakai atau belum
        # belum bisa di cek ada yang kurang cmn masih bingung
        while True:
            input_username = input("Masukkan username jin: ")

            # with open('./FileLoad/Load1/user.csv', 'r') as f:
            #     lines = f.readlines()
            #     i = 0
            #     print(lines)
            # if lines[i] != input_username:
            #     i += 1
                # return
            # jika sudah input lagi username
            print(f"Username “{input_username}” sudah diambil!")
            
            # jika belum masukkan password jin
            while True:
                input_password = input("Masukkan password jin: ")
                x = newLen(input_password)
                # cek panjang nama username
                if x >= 5 or x <= 25:
                    break
            print("Password panjangnya harus 5-25 karakter!")
                
        # print("Mengumpulkan sesajen..")  
        # print("Menyerahkan sesajen...") 
        # print("Membacakan mantra...")   
        
        # print(f" Jin {input_username} berhasil dipanggil! ")
