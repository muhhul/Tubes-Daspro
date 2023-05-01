import function
import time
import sys

def AyamBerkokok (listCandi,user):
    if user=='roro_jonggrang':
        jumlah_candi = 0
        for i in range (1, function.newLen(listCandi)):
            if listCandi[i][0] != '0': #mengecek banyak candi (tidak termasuk yang dihancurkan roro atau hilang bersama dengan jin pembangunnya)
                jumlah_candi += 1

        print (f"Jumlah Candi: {jumlah_candi}")
        if jumlah_candi >= 100:
            print("Yah, Bandung Bondowoso memenangkan permainan!")
        else: 
            print ("Selamat, Roro Jonggrang memenangkan permainan!")
            time.sleep(1.0)
            print ("AAARRRRGGHHHHHH *Bandung Bondowoso angry noise*")
            time.sleep(1.0)
            print ("Roro Jonggrang dikutuk menjadi candi.")
            sys.exit()
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")
