print ("Selamat Datang Di Program Kontak !!!")
nama_kontak = []
nomor_kontak = []
#Daftar Kontak
def daftar():
    if len (nama_kontak) <= 0 :
        print ("Belum ada kontak yang ditambahkan !")
    else :
        for data in range(len(nama_kontak)) :
            print ("Nama Kontak : {} ". format(nama_kontak[data]))
            print ("Nomor Kontak : {} ". format(nomor_kontak[data]))
            print ("--------------------------")

#Menambah kontak
def tambah ():
    tambah_nama = str(input("Nama Kontak : "))
    tambah_nomor = int(input("Nomor Telepon : "))
    if len (tambah_nama) > 0 and len(tambah_nomor) > 0 :
        print ("Kontak berhasil ditambahkan")
        nama_kontak.append(tambah_nama)
        nomor_kontak.append(tambah_nomor)
    else:
        print ("Maaf data yang kamu masukkan salah")

#Tampilan Menu
def tampilan_menu():
    print ("-----Menu-----")
    print ("1. Daftar Kontak")
    print ("2. Tambah Kontak")
    print ("3. Keluar")
    pilih = int(input("Pilih Menu = "))
    if pilih == 1 :
        daftar()
        print("\n")
    elif pilih == 2 :
        tambah()
        print("\n")
    elif pilih == 3 :
        exit("Terimakasih sudah menggunakkan program Kontak, sampai jumpa lagi")
        print ("\n")
    else :
        print ("Maaf menu yang kamu pilih tidak tersedia")
        print("\n")
while (True) :
    tampilan_menu()