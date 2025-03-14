# 📌 1. Kullanıcının girdiği sayının tek mi çift mi olduğunu bulan program
sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
    print(f"{sayi} çifttir.")
else:
    print(f"{sayi} tektir.")

print("\n" + "-"*50)  # Ayırıcı çizgi


# 📌 2. Kullanıcının notunu alarak harf notuna çeviren program
notu = int(input("Notunuzu girin (0-100): "))

if 90 <= notu <= 100:
    harf_notu = "A"
elif 80 <= notu <= 89:
    harf_notu = "B"
elif 70 <= notu <= 79:
    harf_notu = "C"
elif 60 <= notu <= 69:
    harf_notu = "D"
elif 0 <= notu <= 59:
    harf_notu = "F"
else:
    harf_notu = "Geçersiz not!"

print(f"Girdiğiniz nota karşılık gelen harf notu: {harf_notu}")

print("\n" + "-"*50)


# 📌 3. Kullanıcının yaşına göre yaş grubunu belirleyen program
yas = int(input("Yaşınızı girin: "))

if 0 <= yas <= 12:
    yas_grubu = "Çocuk"
elif 13 <= yas <= 19:
    yas_grubu = "Genç"
elif 20 <= yas <= 59:
    yas_grubu = "Yetişkin"
elif yas >= 60:
    yas_grubu = "Yaşlı"
else:
    yas_grubu = "Geçersiz yaş!"

print(f"Yaş grubunuz: {yas_grubu}")

print("\n" + "-"*50)