import function

def ubahPass(user,newPass,listUser):
    for i in range(function.newLen(listUser)):
        if user==listUser[i][0]:
            listUser[i][1]=newPass
            break