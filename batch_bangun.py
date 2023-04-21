import random
def newLen(arr): #pengganti fungsi len
    temp = 0
    for i in arr:
        temp+=1
    return temp
def mencari(arr,nameFile): #untuk meecari apakah ada suatu nilai dalam sebuah list
    cek = False
    for i in range(newLen(arr)):
        if nameFile==arr[i]:
            cek=True
    return cek
def newSplit(arr,x): #pengganti fungsi split
    arrTemp=[[0 for i in range(x)] for j in range(newLen(arr))]
    arrTemp2=['0' for i in range(newLen(arr)-1)]
    for i in range(newLen(arr)):
        kata=''
        count=0
        for j in range(newLen(arr[i])):
            if arr[i][j]==';'or j == newLen(arr[i])-1:
                arrTemp[i][count]=kata
                count+=1
                kata=''
            else:
                kata=kata+arr[i][j]
    return arrTemp

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
def validasi_jumlah_bahan(jumlah_bahan_sekarang, bahan_dibutuhkan): 
    count = 0
    sisa_bahan = [0 for i in range(newLen(jumlah_bahan_sekarang))]
    for bahan in range (newLen(jumlah_bahan_sekarang)): 
        if jumlah_bahan_sekarang[bahan] >= bahan_dibutuhkan[bahan] : 
            count += 1
            
        else: 
            sisa_bahan[bahan] = bahan_dibutuhkan[bahan] - jumlah_bahan_sekarang[bahan]
            count = 0
    if count == 3: 
        return True
    else :
        return sisa_bahan

def batchbangun(user, candi, bahan_bangunan):
    #Menghitung jumlah jin pembangun
    jumlah_jin_pembangun = 0
    nama_jin_pembangun = []
    for baris in range(1, newLen(user)): 
        if user[baris][2] == "jin_pembangun":
            nama_jin_pembangun += [user[baris][0]] 
            jumlah_jin_pembangun += 1
        else: 
            continue
    if jumlah_jin_pembangun == 0: 
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        #menghitung bahan yang dibutuhkan
        jumlah_pasir_dibutuhkan = 0
        jumlah_batu_dibutuhkan = 0
        jumlah_air_dibutuhkan = 0

        array_data_candi = [[0 for i in range (5)] for i in range (jumlah_jin_pembangun)]

        for i in range(jumlah_jin_pembangun): 
            #merandom bahan
            pasir_dibutuhkan = random.randint(1,5)
            batu_dibutuhkan = random.randint(1,5)
            air_dibutuhkan = random.randint(1,5)

            #mengecek id terakhir pada data candi
            id_candi_terakhir = -1
            if newLen(candi) == 1 :
                id_candi_terakhir = -1
            else: 
                id_candi_terakhir = newLen(candi)- 2 
                            
            #menginput data candi
            array_data_candi[i][0] = i + 1 + id_candi_terakhir
            array_data_candi[i][1] = nama_jin_pembangun[i]
            array_data_candi[i][2] = pasir_dibutuhkan
            array_data_candi[i][3] = batu_dibutuhkan
            array_data_candi[i][4] = air_dibutuhkan    

            #menjumlahkan bahan yang dibutuhkan 
            jumlah_pasir_dibutuhkan += pasir_dibutuhkan
            jumlah_batu_dibutuhkan += batu_dibutuhkan
            jumlah_air_dibutuhkan += air_dibutuhkan   

        # print(array_data_candi)
        
        jumlah_bahan_dibutuhkan = [jumlah_pasir_dibutuhkan, jumlah_batu_dibutuhkan, jumlah_air_dibutuhkan]

        print(f"Mengerahkan {jumlah_jin_pembangun} jin untuk membangun candi dengan total bahan {jumlah_pasir_dibutuhkan} pasir, {jumlah_batu_dibutuhkan}, dan {jumlah_air_dibutuhkan} air.")

        # Mengecek ketersediaan bahan yang sudah dikumpulkan
        jumlah_pasir_sekarang = 0
        jumlah_batu_sekarang = 0
        jumlah_air_sekarang = 0
        for baris in range (1, newLen(bahan_bangunan)): 
            if bahan_bangunan[baris][0] == "pasir": 
                jumlah_pasir_sekarang = bahan_bangunan[baris][2]
            elif bahan_bangunan[baris][0] == "batu": 
                jumlah_batu_sekarang = bahan_bangunan[baris][2]
            elif bahan_bangunan[baris][0] == "air": 
                jumlah_air_sekarang = bahan_bangunan[baris][2]
        
        jumlah_bahan = [jumlah_pasir_sekarang, jumlah_batu_sekarang, jumlah_air_sekarang]
        print(jumlah_bahan)

        if validasi_jumlah_bahan(jumlah_bahan, jumlah_bahan_dibutuhkan) == True: 
            print(f"Jin berhasil membangun total {newLen(array_data_candi)} candi")

        else:
            sisa_bahan = validasi_jumlah_bahan (jumlah_bahan, jumlah_bahan_dibutuhkan)
            print(f"Bangun gagal. Kurang {sisa_bahan[0]} pasir, {sisa_bahan[1]} batu, dan {sisa_bahan[2]} air.")
        
        return array_data_candi



#--------------------CONTOH INPUT-----------------------
candi = [["id", "pembuat", "pasir", "batu", "air"], 
         ["0", "pembuat", "12", "11", "11"], 
         ["1", "pembuat", "pasir", "batu", "air"], 
         ["2", "pembuat", "pasir", "batu", "air"]] 

user = [['username','password','role'],
        ['Bondowoso','cintaroro','bandung_bondowoso'],
        ['Roro','gasukabondo','roro_jonggrang'],
        ['jin1','gasukabondo','jin_pembangun'],
        ['jin2','gasukabondo','jin_pembangun'],
        ['jin3','gasukabondo','jin_pembangun'],
        ['jin4','gasukabondo','jin_pembangun']
        ]
bahan_bangunan = [["nama", "deskripsi", "jumlah"], 
                  ["pasir", "bleh2", 1], 
                  ["batu", "bleh2", 1], 
                  ["air", "bleh2", 1]]

batchbangun(user, candi, bahan_bangunan)