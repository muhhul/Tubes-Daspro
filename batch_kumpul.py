import random 
# file = open("Tubes-Daspro/candi.csv", "r")

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
#------------------------------------------------------------------
#-------------------------------------------------------------
#------------------------------------------------------------------
def kumpul() : 

    pasir = random.randint(0,5)
    batu = random.randint(0,5)
    air  = random.randint(0,5)
    # 
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    return [pasir, batu, air]

user = [["usernname", "password", "role"],
        [1, 2, "jin_pengumpul"], 
        [1, 2, "jin_pengumpul"], 
        [1, 2, "jin_pengumpul"]]

def batchkumpul(user):
    jumlah_jin_pengumpul = 0
    for baris in range(1, newLen(user)): 
        if user[baris][2] == "jin_pengumpul":
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
        return Total_kumpul
    else: 
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")










