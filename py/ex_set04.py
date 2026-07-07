# List asal
pekerja = ["Amir", "Siti", "Ali", "Siti", "Raju", "Amir", "Zubaidah"]

# Tulis kod kau di bawah:
nama = set(pekerja)
print(nama)

kelab_bola = {"Ali", "Amir", "Siti", "Raju"}
kelab_badminton = {"Siti", "Zubaidah", "Raju", "Chong"}

#Cari siapa pekerja yang join kedua-dua kelab tersebut (pertembungan ahli).
print(kelab_bola.intersection(kelab_badminton))
print(kelab_bola.difference(kelab_badminton))

#Kau ada satu set barangan runcit yang dah ada kat dapur:

dapur = {"Bawang", "Minyak", "Gula"}

#Kawan kau bawa lagi satu list barang baru:

barang_baru = ["Garam", "Gula", "Kicap"]
#barang_tambah = set(barang_baru) kode ni salah sbb dalam set xleh tambah set lagi so baru belajar pasal update(). update  ni ko buh list ke tuple ke set ke dia boleh direct masukkan sbb update ni xda dalam silibus so dimaafkan lah kalau soalah ni agak mencabar.
dapur.update(barang_baru)

# dapur_update = set(dapur)
# print(dapur_update)

print(dapur)

