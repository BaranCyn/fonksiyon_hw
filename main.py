# Metinsel ifade (String)
baslik = "Taşıt Kredisi"

# Metinsel ifadeler çift tırnak veya tek tırnak içinde olabilir:
baslik2 = 'İhtiyaç Kredisi'

# Farklı değişkenlere metinsel ifadeler atayabiliriz:
aciklama = "Bu bir taşıt kredisi açıklamasıdır."

# String değişkenleri print ile yazdırabiliriz:
print(baslik)   # Çıktı: Taşıt Kredisi
print(aciklama) # Çıktı: Bu bir taşıt kredisi açıklamasıdır.
# Tam sayı (Integer) değişken tanımlama
vade = 36  # Kredi vadesi 36 ay

# Farklı tam sayı değişkenleri
ek_vade = 12  # Ek vade süresi

# Tam sayı değişkenleri üzerinde matematiksel işlemler yapabiliriz:
yeni_vade = vade + ek_vade
print(yeni_vade)  # Çıktı: 48
# Float değişken tanımlama (ondalıklı sayı)
aylik_odeme = 1250.75  # Aylık ödeme tutarı

# Ondalıklı sayılarla işlemler yapılabilir:
toplam_geri_odeme = aylik_odeme * vade
print(toplam_geri_odeme)  # Çıktı: 45027.0
# Boolean değişkenler (True/False)
kredi_onaylandi_mi = True  # Kredi onay durumu
# Boolean türünü öğrenme
print(type(kredi_onaylandi_mi))  # Çıktı: <class 'bool'>

# Boolean değişken ile karar verme
if kredi_onaylandi_mi:
    print("Krediniz onaylandı!")
else:
    print("Krediniz onaylanmadı.")

# Boolean değişkenler genellikle karşılaştırmalar ve if bloklarıyla kullanılır
print(kredi_onaylandi_mi)  # Çıktı: True
# Değişkenleri birleştirerek ekrana yazdırma
print("Kredi Türü:", baslik)
print("Vade Süresi:", vade, "ay")
print("Aylık Ödeme:", aylik_odeme, "TL")
# Kullanıcıdan kredi türü bilgisini alma
kredi_turu = input("Hangi kredi türünü almak istiyorsunuz? ")
print("Seçtiğiniz kredi:", kredi_turu)
# Hatalı kullanım:
# print("Toplam ödeme tutarı: " + toplam_geri_odeme)  # TypeError verecektir

# Doğru kullanım: (String'e çevirmek için str() fonksiyonunu kullanabiliriz)
print("Toplam ödeme tutarı: " + str(toplam_geri_odeme))

print(10 + 5)  # Çıktı: 15
print(vade + ek_vade)  # Çıktı: 48
print(10 - 5)  # Çıktı: 5
print(vade - ek_vade)  # Çıktı: 24
print(10 * 5)  # Çıktı: 50
print(vade * 2)  # Çıktı: 72
# Normal bölme (float sonuç)
print(10 / 3)  # Çıktı: 3.3333...

# Tam sayı bölme (integer sonuç)
print(10 // 3)  # Çıktı: 3
# Kalanı bulma
print(10 % 3)  # Çıktı: 1
print(vade % 5)  # Çıktı: 1 (36'nın 5'e bölümünden kalan)



#Mantıksal Operatörler
print(10 == 10)  # Çıktı: True
print(10 != 5)   # Çıktı: True
print(10 > 5)  # Çıktı: True
print(10 < 5)  # Çıktı: False
print(10 > 5 and 5 > 2)  # Çıktı: True
print(10 > 5 and 5 < 2)  # Çıktı: False
print(10 > 5 or 5 < 2)  # Çıktı: True
print(10 < 5 or 5 < 2)  # Çıktı: False

#condition
sayi1 = 10
sayi2 = 15
#indent
if sayi1 > sayi2:
    print("Sayi1 büyüktür.")

#eğer if bloğuna girmez ise
elif sayi1 == sayi2:
    print("iki sayı eşittir")



else:
    print("sayi1 sayi2den büyüktür")
    print("burası if bloğunun dışındadır")

    if sayi1<=sayi2:
    print("Sayi 1 Sayi 2den küçüktür")
    if sayi1<==sayi2:
        print ("Sayi 1 sayi 2ye eşittir")
        else 
        print("Sayi 1 Sayi 2den büyüktür")
        print("burası if bloğunun dışındadır")
        


