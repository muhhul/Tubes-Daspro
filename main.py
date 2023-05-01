# Untuk program utamanya
import importFull
import os
# data csv sudah dipindahkan ke list, tinggal akses seperti list biasa
listUser = importFull.loadSaveExit.user()
listCandi = importFull.loadSaveExit.candi()
listBahan = importFull.loadSaveExit.bahan()
listJin = [['jin','jumlahCandi']]

user=['','']
#importFull.help.help(user)
#importFull.hapusjin.hapusjin(listUser)
#importFull.ubahPassword.ubahPass("Bondowoso","akuMenang",listUser)
#importFull.ubahtipejin.UbahTipeJin(listUser)
#importFull.loadSaveExit.save()


game=True
while(game):
    #os.system('cls')
    inputUser=input(">>> ")
    if inputUser=='help':
        importFull.help.help(user)
    elif inputUser=='login':
        user=importFull.login.login(user,listUser)
    elif inputUser=='logout':
        user=importFull.login.logout(user)
    elif inputUser=='exit':
        importFull.loadSaveExit.exit()
    elif inputUser=='save':
        importFull.loadSaveExit.save()
    elif inputUser=='summonjin':
        importFull.summonjin.summonjin(user[1],listUser,listJin)
    elif inputUser=='hapusjin':
        importFull.hapusjin.hapusjin(listUser,listCandi,user[1],listJin)
    elif inputUser=='ubahjin':
        importFull.ubahtipejin.UbahTipeJin(listUser,user[1])
    elif inputUser=='bangun':
        importFull.bangun.bangun(listBahan,listCandi,user,listJin)
    elif inputUser=='kumpul':
        importFull.kumpul.kumpul(user[1],listBahan)
    elif inputUser=='batchkumpul':
        importFull.batch_kumpul.batchkumpul(user[1],listUser,listBahan)
    elif inputUser=='batchbangun':
        importFull.batch_bangun.batchbangun(user[1],listUser,listCandi,listBahan,listJin)
    elif inputUser=='laporanjin':
        importFull.laporanjin.laporanjin(listUser,listBahan,listJin,user[1])
    elif inputUser=='laporancandi':
        importFull.laporancandi.laporancandi(listCandi,user[1])
    elif inputUser=='hancurkancandi':
        importFull.hancurkancandi.hancurkancandi(listCandi,user[1])
    elif inputUser=='ayamberkokok':
        importFull.ayamberkokok.AyamBerkokok(listCandi,user[1])
    elif inputUser=='ubahpassword':
        importFull.ubahPassword.ubahPass(user[0],listUser)
    else:
        print("Maaf input anda salah, silahkan ketik 'help' untuk command yang valid")
    
