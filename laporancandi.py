import function
import time

def laporancandi(listCandi,user):
    if user == 'bandung_bondowoso': #user merupakan bandung bondowoso
        print ("Mengambil laporan candimu...")
        time.sleep(1.5)
        #total candi
        total_candi = 0
        for i in range (1, function.newLen(listCandi)):
            if listCandi[i][0] != '0':
                total_candi += 1
        print (f"Total candi: {total_candi}")
        time.sleep(0.5)

        #total bahan yang digunakan
        total_pasir = 0
        total_batu = 0
        total_air = 0
        for i in range (1, function.newLen(listCandi)):
            total_pasir += listCandi[i][2]
            total_batu += listCandi[i][3]
            total_air += listCandi[i][4]
        print (f"Total pasir yang digunakan: {total_pasir}")
        time.sleep(0.5)
        print (f"Total batu yang digunakan: {total_batu}")
        time.sleep(0.5)
        print (f"Total air yang digunakan: {total_air}")
        time.sleep(0.5)

        #candi termahal dan termurah
        if total_candi > 0:
            harga_termahal = (10000*listCandi[1][2]) + (15000*listCandi[1][3]) + (7500*listCandi[1][4])
            id_termahal = listCandi [1][0]
            harga_termurah = (10000*listCandi[1][2]) + (15000*listCandi[1][3]) + (7500*listCandi[1][4])
            id_termurah = listCandi [1][0]
            for i in range (1, function.newLen(listCandi)):
                if listCandi [i][0] != '0':
                    harga_candi = (10000*listCandi[i][2]) + (15000*listCandi[i][3]) + (7500*listCandi[i][4])
                    id_candi = listCandi [i][0]
                    if harga_candi > harga_termahal:
                        harga_termahal = harga_candi
                        id_termahal = id_candi
                    else:
                        harga_termahal = harga_termahal
                        id_termahal = id_termahal
                    if harga_candi < harga_termurah:
                        harga_termurah = harga_candi
                        id_termahal = id_candi
                    else :
                        harga_termurah = harga_termurah
                        id_termurah = id_termurah
            print (f"ID Candi Termahal: {id_termahal} (Rp {harga_termahal})")
            time.sleep(0.5)
            print (f"ID Candi Termurah: {id_termurah} (Rp {harga_termurah})")
        else: # total candi = 0
            print (f"ID Candi Termahal: -")
            time.sleep(0.5)
            print (f"ID Candi Termurah: -")
    else: #user bukan bandung bondowoso (roro jonggrang atau jin)
        print ("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")