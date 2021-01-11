from datetime import *

print('Selamat Datang di Perpustakaan')
def dataPinjaman(kode, nama , judul):
    date = datetime.date(datetime.now())
    date2 = date + timedelta(days=7)
    listinput = [kode, nama, judul, str(date), str(date2)]
    file = open("module.txt", 'a')
    file.write('|'.join(listinput))
    file.write('\n')
    file.close()

while True:
    kode = input ('Masukkan Kode Member :')
    nama = input ('Masukkan Nama Member :')
    judul = input ('Masukkan Judul Buku :')
    dataPinjaman(kode,nama,judul)
    again = input('Ulangi lagi (y/n):')
    if again == 'y':
        continue
    elif again == 'n':
        break
    else:
        print('Error')
        break

