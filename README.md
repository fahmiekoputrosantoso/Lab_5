# lab-5
## Latihan 1

* Buat Dictionary daftar kontak
* Tampilkan kontaknya rangga
* tambah kontak baru dengan nama ujang dengan nomor 087645455
* Ubah kontak ayu dengan nomor baru yaitu 0898888667
* Tampilkan semua Nama
* Tampilkan semua nomor
* Tampilkan daftar nama dan nomor
* Hapus kontak ayu

##### Untuk contoh code nya bisa dilihat gambar dibawah ini :

![pict1](assets/Latihan/pict1.PNG)
![pict2](assets/Latihan/pict2.PNG)

# Hasil Output :
#### Daftar kontak :
* Output menampilkan daftar kontak berdasarkan

![pict3](assets/Latihan/pict3.PNG)

#### Menambah kontak baru Ujang :
* Output menambahkan kontak baru ujang

![pict4](assets/Latihan/pict4.PNG)

#### Ubah kontak ayu :
* Output mengubah kontak dina dengan nomor baru

![pict5](assets/Latihan/pict5.PNG)

#### Tampilkan semua nama :
* Output menampilkan semua Nama

![pict6](assets/Latihan/pict6.PNG)

#### Tampilkan semua nomor :
* Output menampilkan semua nomor

![pict7](assets/Latihan/pict7.PNG)

#### Tamplikan daftar nama dan nomor :
* Output menampilkan semua nama dan nomor

![pict8](assets/Latihan/pict8.PNG)

#### Hapus kontak ayu :
* Output menghapus kontak ayu

![pict9](assets/Latihan/pict9.PNG)

## Tugas Praktikum 5

![Gambar1](assets/TugasPraktikum/Gambar1.PNG)

**Code:**

![Gambar2](assets/TugasPraktikum/Gambar2.PNG)
![Gambar3](assets/TugasPraktikum/Gambar3.PNG)
![Gambar4](assets/TugasPraktikum/Gambar4.PNG)
![Gambar5](assets/TugasPraktikum/Gambar5.PNG)
![Gambar6](assets/TugasPraktikum/Gambar6.PNG)
![Gambar7](assets/TugasPraktikum/Gambar7.PNG)

**Penjelasan:**

**Header**
* ``data={}`` list dengan format dictionary
* Gunakanlah perulangan ``While`` untuk menampilkan data sebanyak banyaknya
* ``menu = input("(T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar: ")`` kita tambahkan input Tambah, Ubah, Hapus, Lihat, Cari, Keluar dalam variabel menu
* ``else: print("Upss ada yang salah, silahkan cek kembali.")`` jika kita salah dalam input maka akan tercetak 'Upss ada yang salah, silahkan cek kembali.'
* masukan nama, nim, nilai_tugas, nilai_uts, nilai_uas, dan nilai_akhir yang nanti akan di masukkan kedalam ``data={}``
* Nilai akhir didapat dari = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100

**Keluar**
* ``if menu.lower() == 'k':`` Ambil data 'k' dari ``menu``
* lalu ``break`` untuk menghentikan seluruh proses

**Lihat data**
* ``elif menu.lower() == 'l':`` Kita menggunakan kondisi percabangan if, ambil data dari ``menu`` lalu kita akan mengubah perintah 'l' yang kita input menjadi huruf kecil dengan fungsi ``lower()``
* lalu cetak ``print()``

**Tambah data**
* ``elif menu.lower() == 't':`` Ambil data 't' dari ``menu``
* ``nama = input("Masukan nama: ")`` lalu tambahkan input nama, nim, nilai tugas, uts, uas
* ``nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 `` untuk nilai akhir diambil dari perhitungan 3 komponen nilai (nilai_tugas: 30%, nilai_uts: 35%, nilai_uas: 35%)
* ``data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir]`` kita akan masukkan data yang tadi kita input ke dalam `data[nama]'
* lalu cetak ``print()``

**Ubah data**
* ``elif menu.lower() == 'u':`` Ambil data 'u' dari ``menu``
* ``nama = input("Masukan nama untuk mengubah data: ")`` kita akan menginput data yang nanti akan di ubah
* ``if nama in data.keys(): print("Mau mengubah apa?")`` jika 'nama' dari di dalam 'data' maka akan mengembalikan daftar menggunakan fungsi 'keys()' lalu di cetak lah 'print()'
* ``sub_data = input("(Semua), (Nama), (NIM), (Tugas), (UTS), (UAS) : ")`` memmbuat menu ubah di dalam ``sub_data``
* ``if sub_data.lower() == "semua":`` ambil kata kunci 'semua' di dalam ``sub_data`` jika 'semua' maka input ``data[nama][1] = input("Ubah NIM:") data[nama][2] = int(input("Ubah Nilai Tugas: ")) data[nama][3] = int(input("Ubah Nilai UTS: ")) data[nama][4] = int(input("Ubah Nilai UAS: "))``
* ``data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100 `` kita dapatkan nilai akhir dengan diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%),

*ket: [5] = nilai_akhir, dimana [0] = nama*

* lalu cetak ``print("\nBerhasil ubah data!")``
* Jika kita ingin mengubah data tertentu maka ``elif sub_data.lower() == "nim": data[nama][1] = input("NIM:")`` dan berlaku juga untuk nilai tugas, UTS dan UAS
* lalu cetak ``print("\nBerhasil ubah data!")``
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika kita salah dalam memasukkan nama untuk mengubah data maka akan muncul 'nama tidak di temukan'

**Cari data**
* ``elif menu.lower() == 'c':`` Ambil data 'c' dari ``menu``
* ``nama = input("Masukan nama untuk mencari data: ")`` kita akan menginput data yang nanti akan di cari
* ``if nama in data.keys():`` kita mengambil list 'nama' di dalam 'data' menggunakan pengkondisian
* maka cetak ``print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5}"`` untuk menampilkan data yang tersedia
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika data yang kita input salah/tidak ditemukan maka akan tercetak 'nama tidak di temukan'

**Hapudata**
* ``elif menu.lower() == 'h':`` Ambil data 'h' dari ``menu``
* ``nama = input("Masukan nama untuk menghapus data : ")`` kita akan menginput data yang nanti akan di hapus
* ``if nama in data.keys():`` kita mengambil list 'nama' di dalam 'data' menggunakan pengkondisian
* ``del data[nama]`` hapus semua 'nama'  yang ada di dalam 'data'
* jika sudah maka cetak ``print("sub_data '{}' berhasil dihapus.".format(nama))``
* ``else: print("'{}' tidak ditemukan.".format(nama))`` jika data yang kita input salah/tidak ditemukan maka akan tercetak 'nama tidak di temukan'



**Output:**

Tambah data

![Gambar8](assets/TugasPraktikum/Gambar8.PNG)


Ubah data

![Gambar9](assets/TugasPraktikum/Gambar9.PNG)


Lihat data

![Gambar10](assets/TugasPraktikum/Gambar10.PNG)


Cari data

![Gambar11](assets/TugasPraktikum/Gambar11.PNG)


Hapus data

![Gambar12](assets/TugasPraktikum/Gambar13.PNG)


**Flowchart:**


![Flowchart](assets/TugasPraktikum/flowchart.png)
