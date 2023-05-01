import function

def laporanjin(listUser,listBahan,listJin,user,listCandi):
    if user == 'bandung_bondowoso':
        totalJin = 0
        totalJinPengumpul = 0
        totalJinPembangun = 0
        jinTerajin = ''
        jinTermalas = ''
        candiTerajin=0
        candiTermalas=9999
        for i in range(function.newLen(listUser)):
            if listUser[i][2] == "pengumpul" and listUser[i][0] != '0':
                totalJinPengumpul += 1  
            elif listUser[i][2] == "pembangun" and listUser[i][0] != '0':
                totalJinPembangun += 1
            totalJin = totalJinPengumpul + totalJinPembangun
        for i in range(3,function.newLen(listUser)):
            if listUser[i][2]=='pembangun':
                temp=[listUser[i][0],0]
                listJin.append(temp)
        for i in range(1,function.newLen(listCandi)):
            for j in range(1,function.newLen(listJin)):
                if listCandi[i][1]==listJin[j][0]:
                    listJin[j][1]=(int(listJin[j][1]+1))
        for i in range(1,function.newLen(listJin)):
            if listJin[i][0]!='0':
                if int(listJin[i][1])<=int(candiTermalas):
                    if int(listJin[i][1])==int(candiTermalas):
                        if listJin[i][0]>jinTermalas:
                            jinTermalas=listJin[i][0]
                    else:
                        candiTermalas=listJin[i][1]
                        jinTermalas=listJin[i][0]
                if int(listJin[i][1])>=int(candiTerajin):
                    if int(listJin[i][1])==int(candiTerajin):
                        if listJin[i][0]<jinTerajin:
                            jinTerajin=listJin[i][0]
                    else:
                        candiTerajin=listJin[i][1]
                        jinTerajin=listJin[i][0]
        print(f"Total Jin: {totalJin}")
        print(f"Total Jin Pengumpul: {totalJinPengumpul}")
        print(f"Total Jin Pembangun: {totalJinPembangun}")
        print(f"Jin Terajin: {jinTerajin}")
        print(f"Jin Termalas: {jinTermalas}")
        print(f"Jumlah Pasir: {listBahan[1][2]} unit")
        print(f"Jumlah Air: {listBahan[2][2]} unit")
        print(f"Jumlah Batu: {listBahan[3][2]} unit")
    else: #user != "Bandung Bondowoso"
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
