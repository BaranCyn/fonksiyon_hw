# Fonksiyonlar Ödevi

# 1️⃣ Hesap Makinesi Fonksiyonu
def hesap_makinesi(a, b):
    toplam = a + b
    fark = a - b
    carpim = a * b
    bolum = a / b if b != 0 else "Tanımsız"  # Sıfıra bölme hatasını önlemek için kontrol
    return toplam, fark, carpim, bolum

# Kullanıcıdan iki sayı alıp fonksiyonu çalıştırma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
t, f, c, b = hesap_makinesi(sayi1, sayi2)
print(f"Toplam: {t}, Fark: {f}, Çarpım: {c}, Bölüm: {b}")

# 2️⃣ Palindrom Kontrol Fonksiyonu
def palindrom_mu(kelime):
    kelime = kelime.lower()  # Büyük/küçük harf duyarlılığını kaldır
    return kelime == kelime[::-1]  # Tersini alarak karşılaştır

# Kullanıcıdan kelime alıp kontrol etme
kelime = input("Bir kelime girin: ")
if palindrom_mu(kelime):
    print(f"'{kelime}' bir palindromdur.")
else:
    print(f"'{kelime}' bir palindrom değildir.")

# 3️⃣ 100 Yaşına Ulaşma Hesaplama Fonksiyonu
def kac_yil_sonra_100_olur(yas):
    kalan_yil = 100 - yas
    return kalan_yil if kalan_yil > 0 else "Zaten 100 yaşını geçmişsiniz!"

# Kullanıcıdan yaş alıp hesaplama
yas = int(input("Yaşınızı girin: "))
print(f"{kac_yil_sonra_100_olur(yas)} yıl sonra 100 yaşına ulaşacaksınız.")