import random 
# file = open("Tubes-Daspro/candi.csv", "r")

def kumpul(user,listBahan):
    if user=='pengumpul': 
        pasir = random.randint(0,5)
        batu = random.randint(0,5)
        air  = random.randint(0,5)
        # 
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
        listBahan[1][2]=str(int(listBahan[1][2])+pasir)
        listBahan[2][2]=str(int(listBahan[2][2])+batu)
        listBahan[3][2]=str(int(listBahan[3][2])+air)
    else:
        print("Maaf anda tidak bisa mengakses fitur ini")






