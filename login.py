from typing import List
import function

# logged_user = [USERNAME, PASSWORD, ROLE]
# Jika tidak login -> logged_user = ["", "", ""]


def login(logged_user: List[str],listUser) -> List[str]:
    # 1. Check login, jika sudah login, gagal
    if logged_user != '':
        print("Anda masih login")
    # 2. Belum login?, input username dan password
    else:
        input_username = input("Username: ")
        input_password = input("Password: ")
        # 3. Bandingkan dengan CSV
        for i in range(function.newLen(listUser)):
            # Skip CSV header
            if listUser[i][0] == input_username:
            # - Jika password salah, print password salah
                if listUser[i][1] != input_password:
                    print("Password salah")
                else:
                    # - Jika benar, print Selamat datang
                    print("Selamat datang")
                    print("")
                    return [listUser[i][0], listUser[i][2]]
            # - Jika username salah, print username tidak terdaftar
            elif i+1==function.newLen(listUser):
                # Tangkap break dari for loop
                print("Username tidak terdaftar")

# if __name__ == "__main__":
#     logged_user = ["", "", ""]
#     asd = login(logged_user)

# logout

def logout(logged_user: List[str]):
    # mengecek masih login atau blm
    if logged_user == '':
        # jika blm print(blm login)
        print("logout gagal")
        print("anda belum login")
    # jika sudah print(logout)
    else:
        print("logout")
        return ['','']
