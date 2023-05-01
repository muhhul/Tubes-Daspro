import random 
from function import newLen, newAppend,cek_id
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def validasi_jumlah_bahan(jumlah_bahan_sekarang, bahan_dibutuhkan): 
    count = 0
    sisa_bahan = [0 for i in range(newLen(jumlah_bahan_sekarang))]
    for bahan in range (newLen(jumlah_bahan_sekarang)): 
        if int(jumlah_bahan_sekarang[bahan]) >= int(bahan_dibutuhkan[bahan]) : 
            count += 1
            
        else: 
            sisa_bahan[bahan] = int(bahan_dibutuhkan[bahan]) - int(jumlah_bahan_sekarang[bahan])
            count = 0
    if count == 3: 
        return True
    else :
        return sisa_bahan




def bangun (listBahan,listCandi,user,listJin):
    if user[1]=='pembangun':
        if newLen(listCandi) > 1: 
            list_id = cek_id(listCandi)             
        else: 
            list_id = [i for i in range (1,101)]
        
        pasir = random.randint(1,5)
        batu = random.randint(1,5)
        air  = random.randint(1,5)
        bahan_dibutuhkan =[pasir, batu, air]

        #print(f"Men-generate bahan bangunan ({pasir} pasir, {batu} batu, dan {air} air)")

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
        
        if validasi_jumlah_bahan(jumlah_bahan, bahan_dibutuhkan) == True:
            for i in range(newLen(listJin)):
                if user[0]==listJin[i][0]:
                    listJin[i][1]=str(int(listJin[i][1])+1)
            for i in range(newLen(listCandi)):
                id_candi = 0
                if listCandi[i][0]=='0':
                    listCandi[i][0]=f'{i+1}'
                    listCandi[i][1]=user[0]
                    listCandi[i][2]=bahan_dibutuhkan[0]
                    listCandi[i][3]=bahan_dibutuhkan[1]
                    listCandi[i][4]=bahan_dibutuhkan[2]
                    break
                elif i+1==newLen(listCandi):
                    for j in range (1, 101):
                        if list_id[j-1] == j:
                            id_candi = j
                            list_id[j-1] = ''
                            break
                        else: 
                            continue
                    temp=[f'{id_candi}',user[0],bahan_dibutuhkan[0],bahan_dibutuhkan[1],bahan_dibutuhkan[2]]
                    listCandi = newAppend(listCandi, temp)
                    # listCandi.append(temp)
                    # print(listCandi)
            listBahan[1][2] = int(jumlah_pasir_sekarang) - int(bahan_dibutuhkan[0])
            listBahan[2][2] = int(jumlah_batu_sekarang) - int(bahan_dibutuhkan[1])
            listBahan[3][2] = int(jumlah_air_sekarang) - int(bahan_dibutuhkan[2])

            print("Candi berhasil dibangun")
            count=0
            for i in range(1,newLen(listCandi)):
                if listCandi[i][0]!='0':
                    count+=1
            sisa_candi = 100 - (count)
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
#          ["1", "pembuat", "pasir", "batu", "air"], 
#          ["3", "pembuat", "pasir", "batu", "air"], 
#          ["5", "pembuat", "pasir", "batu", "air"]]     

# bangun(bahan_bangunan, candi)




