# Fungsi untuk menghitung luas permukaan balok
def luas_permukaan_balok(p, l, t):
    # Rumus luas permukaan balok = 2 * (p*l + p*t + l*t)
    return 2 * (p*l + p*t + l*t)

# Fungsi untuk menghitung volume balok
def volume_balok(p, l, t):
    # Rumus volume balok = p * l * t
    return p * l * t

# Contoh penggunaan fungsi
# Masukkan panjang, lebar, dan tinggi balok
p = float(input("Masukkan panjang balok: "))
l = float(input("Masukkan lebar balok: "))
t = float(input("Masukkan tinggi balok: "))
# Panggil fungsi luas_permukaan_balok dan volume_balok
# Cetak hasilnya dengan pembulatan dua angka di belakang koma
print(f"Luas permukaan balok = {round(luas_permukaan_balok(p, l, t), 2)}")
print(f"Volume balok = {round(volume_balok(p, l, t), 2)}")
