from typing import List

# logged_user = [USERNAME, PASSWORD, ROLE]
# Jika tidak login -> logged_user = ["", "", ""]


def login(logged_user: List[str]) -> List[str]:
    # 1. Check login, jika sudah login, gagal
    if logged_user[0] != "":
        print("Anda masih login")
        return ["", "", ""]
    # 2. Belum login?, input username dan password
    input_username = input("Username: ")
    input_password = input("Password: ")
    # 3. Bandingkan dengan CSV
    with open("./FileLoad/Load1/user.csv") as f:
        rows = f.read().splitlines()
        # Loop CSV
        for i in range(rows):
            row = rows[i]
            # TODO: Aldi: NewSplit bermasalah, sampai dibenarkan, akan memakai split
            [ctx_username, ctx_password, ctx_role] = row.split(";")

            # Skip CSV header
            if i == 0:
                continue
            # - Jika username salah, print username tidak terdaftar
            if ctx_username != input_username:
                continue
            # - Jika password salah, print password salah
            if ctx_password != input_password:
                print("Password salah")
                return ["", "", ""]

            # - Jika benar, print Selamat datang
            print("Selamat datang")
            print("")
            return [ctx_username, ctx_password, ctx_role]
    # Tangkap break dari for loop
    print("Username tidak terdaftar")
    return ["", "", ""]


# if __name__ == "__main__":
#     logged_user = ["", "", ""]
#     asd = login(logged_user)

# logout


def logout(logged_user: List[str]):
    # mengecek masih login atau blm
    if logged_user[0] == "":
        # jika blm print(blm login)
        print("logout gagal")
        print("anda belum login")
        return
    # jika sudah print(logout)
    print("logout")
