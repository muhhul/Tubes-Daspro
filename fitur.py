# Untuk membuat fitu seperti load, login, dll

import argparse
import sys

parser = argparse.ArgumentParser(description='Masukkan Nama Folder')
parser.add_argument('namaFolder', type=str, nargs = '?', help='Nama Folder', default='')
args = parser.parse_args()

if args.namaFolder=='Tubes':
    print("Loading")
elif args.namaFolder=='':
    print("Tidak ada nama folder yang diberikan")
    sys.exit()
else:
    print("Nama Folder salah")
    sys.exit()