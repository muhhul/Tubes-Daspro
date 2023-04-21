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






