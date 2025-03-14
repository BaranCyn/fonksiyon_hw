# 📌 1. Kullanıcıdan ad, yaş ve doğum yılını alarak ekrana yazdıran program
ad = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))
dogum_yili = 2024 - yas  # Doğum yılını hesapla

print(f"Merhaba {ad}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")

print("\n" + "-"*50)  


# 📌 2. Kullanıcıdan iki sayı alarak işlem yapan program
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
if sayi2 != 0:
    bolum = sayi1 / sayi2
else:
    bolum = "Tanımsız (sıfıra bölme hatası)"

print(f"\nToplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")

print("\n" + "-"*50)