import function

def laporanjin(listUser):
    if user == "Bandung Bondowoso":
        totalJin = 0
        totalJinPengumpul = 0
        totalJinPembangun = 0
        jinTerajin = 0
        jinTermalas = 0
        totalPasir = 0
        totalAir = 0
        totalBatu = 0
        for i in range(function.newLen(listUser)):
            if listUser[i][3] == "pengumpul":
                totalJinPengumpul += 1  
            elif listUser[i][3] == "pembangun":
                totalJinPembangun += 1
            totalJin = totalJinPengumpul + totalJinPembangun
    
    print(f"Total Jin: {totalJin}")
    print(f"Total Jin Pengumpul: {totalJinPengumpul}")
    print(f"Total Jin Pembangun: {totalJinPembangun}")
    print(f"Jin Terajin: {jinTerajin}")
    print(f"Jin Termalas: {jinTermalas}")
    print(f"Jumlah Pasir: {totalPasir} unit")
    print(f"Jumlah Air: {totalAir} unit")
    print(f"Jumlah Batu: {totalBatu} unit")
    else: #user != "Bandung Bondowoso"
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    
    #blmBeresss
