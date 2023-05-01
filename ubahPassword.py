import function

def ubahPass(user,listUser):
    if user != '':
        newPass=input("Masukkan password baru: ")
        for i in range(function.newLen(listUser)):
            if user==listUser[i][0]:
                listUser[i][1]=newPass
                print ("Password berhasil diubah.")
                break
    else:
        print("Maaf anda belum login")
