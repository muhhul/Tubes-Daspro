# Untuk program membuat fungsi built in seperti pengganti append.()

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

def newAppend(arr1,arr2): 
    temp = [[0 for i in range(newLen(arr2))] for j in range(newLen(arr1)+1)]
    for j in range(newLen(arr1)+1):
        for i in range(newLen(arr2)): 
            if j <= newLen(arr1)-1 : 
                temp[j][i] = arr1[j][i]
            else: 
                temp[j][i] = arr2[i]
    return(temp)

# listCandi = [["id", "pembuat", "pasir", "batu", "air"], 
#          ["1", "pembuat", "pasir", "batu", "air"], 
#          ["3", "pembuat", "pasir", "batu", "air"], 
#          ["5", "pembuat", "pasir", "batu", "air"]] 


def cek_id (listCandi): 
    list_id = [i for i in range(1,101)]
    for i in range(100):
        for j in range(1, newLen(listCandi)):
            if list_id[i] == int(listCandi[j][0]) : 
                list_id[i] = ''
    return(list_id)

