import random 
from function import newLen
#------------------------------------------------------------------
#-------------------------------------------------------------
#------------------------------------------------------------------
def kumpul() : 

    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air  = random.randint(0,5)
    return [pasir, batu, air]

def batchkumpul(user,listUser,listBahan):
    if user=='bandung_bondowoso':
        jumlah_jin_pengumpul = 0
        for baris in range(1, newLen(listUser)): 
            if listUser[baris][2] == 'pengumpul':
                jumlah_jin_pengumpul += 1
            else: 
                continue
        print(f"Mengerahkan {jumlah_jin_pengumpul} jin untuk mengumpulkan bahan")
        if jumlah_jin_pengumpul > 0 :
            Total_kumpul = [0,0,0]
            for i in range(jumlah_jin_pengumpul): 
                bahan_kumpul = kumpul()
                for bahan in range(3):
                    Total_kumpul[bahan] += bahan_kumpul[bahan]
            pasir = Total_kumpul[0]
            batu = Total_kumpul[1]
            air = Total_kumpul[2]

            print(f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air")
            listBahan[1][2]=str(int(listBahan[1][2])+pasir)
            listBahan[2][2]=str(int(listBahan[2][2])+batu)
            listBahan[3][2]=str(int(listBahan[3][2])+air)
        else: 
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")











