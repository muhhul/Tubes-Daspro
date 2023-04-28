import function

def summonjin(user,listUser,listJin):
    # cek user bondowoso atau bkn?
    if user =='bandung_bondowoso':
        count = 0
        for i in range(function.newLen(listJin)):
            if listJin[i][0]!='0':
                count += 1

        if count > 100:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            return
        # jika iya (summon jenis jin)
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        
        role_jin_pengumpul = 1
        role_jin_pembangun = 2
        # jika tidak input jenis lagi
        jin=''
        while True:
            input_role = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            if input_role == role_jin_pengumpul:
                print("Memilih jin \"Pengumpul\"")
                jin='pengumpul'
                break
            if input_role == role_jin_pembangun:
                print("Memilih jin \"pembangun\"")
                jin='pembangun'
                break
            print(f"Tidak ada jenis jin bernomor \"{input_role}\"!")
        # jika iya pilih jin dan masukan nama user
        # cek nama user sudah dipakai atau belum
        # belum bisa di cek ada yang kurang cmn masih bingung
        while True:
            input_username = input("Masukkan username jin: ")
            cek=False
            for i in range(function.newLen(listUser)):
                if listUser[i][0]==input_username:
                    cek=True
            if cek==False:
                break
            print(f"Username “{input_username}” sudah diambil!")
            
            # jika belum masukkan password jin
        while True:
            input_password = input("Masukkan password jin: ")
            x = function.newLen(input_password)
            # cek panjang nama username
            if x >= 5 or x <= 25:
                break
            print("Password panjangnya harus 5-25 karakter!")
                
        temp=[input_username,input_password,jin]
        listUser.append(temp)
        temp=[input_username,0]
        listJin.append(temp)
        print("Mengumpulkan sesajen..")  
        print("Menyerahkan sesajen...") 
        print("Membacakan mantra...")   
        
        print(f" Jin {input_username} berhasil dipanggil! ")
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")
