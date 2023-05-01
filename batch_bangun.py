import random
from function import newLen, newAppend, cek_id

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

def batchbangun(user, listUser,listCandi, listBahan,listJin):
    #Menghitung jumlah jin pembangun
    if user=='bandung_bondowoso':
        if newLen(listCandi) > 1: 
            list_id = cek_id(listCandi)             
        else: 
            list_id = [i for i in range (1,101)]        
        jumlah_jin_pembangun = 0
        nama_jin_pembangun = []
        for baris in range(1, newLen(listUser)): 
            if listUser[baris][2] == 'pembangun':
                nama_jin_pembangun += [listUser[baris][0]] 
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
                id_candi = 0

                #mengecek id yang tersedia
                for j in range (1, 101):
                    if list_id[j-1] == j:
                        id_candi = j
                        list_id[j-1] = ''
                        break
                    else: 
                        continue
                                
                #menginput data candi
                array_data_candi[i][0] = id_candi
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

            print(f"Mengerahkan {jumlah_jin_pembangun} jin untuk membangun candi dengan total bahan {jumlah_pasir_dibutuhkan} pasir, {jumlah_batu_dibutuhkan} batu, dan {jumlah_air_dibutuhkan} air.")

            # Mengecek ketersediaan bahan yang sudah dikumpulkan
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

            if validasi_jumlah_bahan(jumlah_bahan, jumlah_bahan_dibutuhkan) == True: 
                print(f"Jin berhasil membangun total {newLen(array_data_candi)} candi")
                for i in range(newLen(array_data_candi)):
                    listCandi = newAppend(listCandi,array_data_candi[i])
                for i in range(1,newLen(listJin)):
                    listJin[i][1]=(int(listJin[i][1]))+1
                listBahan[1][2] = int(jumlah_pasir_sekarang) - int(jumlah_pasir_dibutuhkan)
                listBahan[2][2] = int(jumlah_batu_sekarang) - int(jumlah_batu_dibutuhkan)
                listBahan[3][2] = int(jumlah_air_sekarang) - int(jumlah_air_dibutuhkan)
            else:
                sisa_bahan = validasi_jumlah_bahan (jumlah_bahan, jumlah_bahan_dibutuhkan)
                print(f"Bangun gagal. Kurang {sisa_bahan[0]} pasir, {sisa_bahan[1]} batu, dan {sisa_bahan[2]} air.")
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")