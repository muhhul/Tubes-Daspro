import function
def hancurkancandi (listCandi):
   id_candi = int(input("Masukkan ID candi: "))
   for i in range(function.newLen(listCandi)):
    if id_candi == listCandi[i][0]:
        print(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)")
        choice = input("(Y/N)?")
        if choice == 'Y':
            print("Candi telah berhasil dihancurkan")
            listCandi[i][0]='0'
            candi_terhapus = i
        else:
            print("Candi batal dihancurkan")
        break
    elif i+1 == function.newLen(listCandi):
        print("Tidak ada candi dengan ID tersebut.")
