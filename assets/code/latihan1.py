daftar_kontak = {}

#rangga
daftar_kontak['rangga'] = '081268778'
daftar_kontak['ayu'] = '087688877'
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

#ayu
daftar_kontak['ayu'] = '087688877'

#ujang
daftar_kontak['ujang'] = '087645455'
daftar_kontak['rangga'] = '081268778'
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

#ubah kontak ayu
daftar_kontak['ayu'] = '0898888667'
daftar_kontak['rangga'] = '081278668'
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

#tampilkan semua nama
for nama in daftar_kontak.keys():
    print(nama)
print('+--------------------------+\n')

#tampilkan semua nomor
for nomor in daftar_kontak.values():
    print(nomor)
print('+--------------------------+\n')

#tampilkan daftar nama dan nomor
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
    print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')

#hapus kontak ayu
del daftar_kontak['ayu']
daftar_kontak['rangga'] = '081278668'
print("# Nama   | Nomor telepon")
print("# ========================")
for i in daftar_kontak.items():
     print("# {0:6} |".format(i[0]),i[1])
print('+--------------------------+\n')
