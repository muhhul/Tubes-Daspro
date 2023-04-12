def hapusjin ():
    jin = input("Masukkan username jin: ")
    if jin == ketemu:
        print("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)?")
        choice = input("(Y/N)?")
        if choice == 'Y':
            print("Jin telah berhasil dihapus dari alam gaib.")
        else:
            print("Jin batal dihapus.")
    else:
        print("Tidak ada jin dengan username tersebut.")