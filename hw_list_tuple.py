# Listeler ve Tuple'lar Ödevi

# 1️⃣ Kullanıcıdan 5 sayı alarak toplam, ortalama, en büyük ve en küçük elemanı bulma
def sayi_listesi_islemleri():
    numbers = []
    for i in range(5):
        num = float(input(f"{i+1}. sayıyı girin: "))
        numbers.append(num)

    toplam = sum(numbers)
    ortalama = toplam / len(numbers)
    en_buyuk = max(numbers)
    en_kucuk = min(numbers)

    print("\nGirilen Sayılar:", numbers)
    print(f"Toplam: {toplam}")
    print(f"Ortalama: {ortalama}")
    print(f"En Büyük: {en_buyuk}")
    print(f"En Küçük: {en_kucuk}")
    print("-" * 30)

# 2️⃣ Kullanıcıdan kelimeler alıp listeye ekleyerek ters sıralama
def kelime_listesi():
    kelimeler = []
    kelime_sayisi = int(input("Kaç kelime gireceksiniz? "))

    for i in range(kelime_sayisi):
        kelime = input(f"{i+1}. kelimeyi girin: ")
        kelimeler.append(kelime)

    kelimeler.reverse()
    print("\nTers sıralanmış kelimeler:", kelimeler)
    print("-" * 30)

# 3️⃣ Bir listeden tekrar eden elemanları kaldırma
def tekrar_edenleri_kaldir():
    orijinal_liste = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
    benzersiz_liste = list(set(orijinal_liste))

    print("\nOrijinal Liste:", orijinal_liste)
    print("Tekrar Edenler Kaldırıldıktan Sonra:", benzersiz_liste)
    print("-" * 30)

# Ana program
if __name__ == "__main__":
    sayi_listesi_islemleri()
    kelime_listesi()
    tekrar_edenleri_kaldir()