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



### output dari bangun masih berupa bahan yang dibutuhkan untuk membuat candi, gua belom tau bentuk array dari user yang aktif kek gimana buat bisa ngasih ouput id dan nama pembuat

def bangun (listBahan,listCandi,user,listJin):
    if user[1]=='pembangun':
        pasir = random.randint(1,5)
        batu = random.randint(1,5)
        air  = random.randint(1,5)
        bahan_dibutuhkan =[pasir, batu, air]

        print(f"Men-generate bahan bangunan ({pasir} pasir, {batu} batu, dan {air} air)")

        jumlah_pasir_sekarang = 0
        jumlah_batu_sekarang = 0
        jumlah_air_sekarang = 0
        for baris in range (1, newLen(listBahan)): 
            if listBahan[baris][0] == "pasir": 
                jumlah_pasir_sekarang = listBahan[baris][2]
            elif listBahan[baris][0] == "batu": 
                jumlah_batu_sekarang = listBahan[baris][2]
            elif listBahan[baris][0] == "air": 
                jumlah_air_sekarang = listBahan[baris][2]
        
        jumlah_bahan = [jumlah_pasir_sekarang, jumlah_batu_sekarang, jumlah_air_sekarang]
        print(jumlah_bahan)
        
        if validasi_jumlah_bahan(jumlah_bahan, bahan_dibutuhkan) == True:
            for i in range(newLen(listJin)):
                if user[0]==listJin[i][0]:
                    listJin[i][1]=str(int(listJin[i][1])+1)
            for i in range(newLen(listCandi)):
                if listCandi[i][0]=='0':
                    listCandi[i][0]=f'{i+1}'
                    listCandi[i][1]=user[0]
                    listCandi[i][2]=bahan_dibutuhkan[0]
                    listCandi[i][3]=bahan_dibutuhkan[1]
                    listCandi[i][4]=bahan_dibutuhkan[2]
                    break
                elif i+1==newLen(listCandi):
                    temp=[f'{i+2}',user[0],bahan_dibutuhkan[0],bahan_dibutuhkan[1],bahan_dibutuhkan[2]]
                    listCandi.append(temp)

            print("Candi berhasil dibangun")
            count=0
            for i in range(newLen(listCandi)):
                if listCandi[i][0]!='0':
                    count+=1
            sisa_candi = 100 - count
            print(f"Sisa candi yang perlu dibangun: {sisa_candi}")
        else: 
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")


#----------------CONTOH INPUT------------------------------#
# bahan_bangunan = [["nama", "deskripsi", "jumlah"], 
#                   ["pasir", "bleh2", 12], 
#                   ["batu", "bleh2", 12], 
#                   ["air", "bleh2", 12]]
# candi = [["id", "pembuat", "pasir", "batu", "air"], 
#          ["id", "pembuat", "pasir", "batu", "air"], 
#          ["id", "pembuat", "pasir", "batu", "air"], 
#          ["id", "pembuat", "pasir", "batu", "air"]]     

#bangun(bahan_bangunan, candi)




