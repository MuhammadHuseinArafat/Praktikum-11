import datetime

def cari(kode):
    daftar = [] 
    file = open('module.txt','r')
    dft = [str(i) for i in file.readlines()]
    for data in dft:
        data = data.replace("\n","")
        data = data.split("|")
        daftar.append(data)

    for n in daftar:
        if kode in n:
            print("-" * 20)
            print("Data Peminjaman Buku")
            print("-" * 20)
            print("Data berhasil ditemukan :\n",n)
            print("Kode member Anda : ",n[0])
            print("Nama member Anda : ",n[1])
            print("Judul buku Anda : ",n[2])
            print("Tanggal mulai peminjaman Anda : ",n[3])
            print("Tanggal maksimal peminjaman Anda : ",n[4])
            yyyy,mm,dd = [int(i) for i in n[4].split("-")]
            hari = (datetime.datetime(yyyy,mm,dd,0,0,0,0) - datetime.datetime.now()).days
            if hari >= 0:
                print("Sisa waktu peminjaman : ", hari," Hari")
            else :
                terlambat = abs(int((datetime.datetime(yyyy,mm,dd,0,0,0,0) - datetime.datetime.now()).days))
                print("Anda sudah terlambat : ",terlambat," Hari")
                print("Denda : Rp", 2000 * terlambat)
                exit()
                print("Data tidak berhasil ditemukan")

kode = input("Silakan Masukkan Kode Member Anda :")

cari(kode)
