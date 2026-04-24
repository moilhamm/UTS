nama_kandang =""
jumlah_ayam = 0
telur = 0

nama_kandang = input("masukkan nama kandang : ")
jumlah_ayam = int(input("Masukan Jumlah Ayam : "))

for hari in range(1,8):
  telur_hari_ini = int(input(f"Masukan Jumlah telur hari ke-{hari} : "))
  telur = telur + telur_hari_ini

rata_rata = telur / jumlah_ayam

if rata_rata >= 0.8:
  kategori = "Produktif Tinggi"
elif rata_rata >= 0.5 and rata_rata < 0.79:
  kategori = "Produktif Sedang"
else:
  kategori = "Produktif Rendah"

print(f"Nama Kandang : {nama_kandang}")
print(f"Jumlah Ayam : {jumlah_ayam}")
print(f"Rata-rata Telur : {rata_rata}")
print(f"Kategori Produksi : {kategori}")