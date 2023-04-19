# Untuk program utamanya
import importFull
# data csv sudah dipindahkan ke list, tinggal akses seperti list biasa
listUser = importFull.loadSaveExit.user()
listCandi = importFull.loadSaveExit.candi()
listBahan = importFull.loadSaveExit.bahan()

user=''
importFull.help.help(user)
importFull.hapusjin.hapusjin(listUser)
#importFull.ubahPassword.ubahPass("Bondowoso","akuMenang",listUser)
importFull.ubahtipejin.UbahTipeJin(listUser)
importFull.loadSaveExit.save()