# 📌 1. 1'den 100'e kadar olan sayıları yazdıran program
print("1’den 100’e kadar olan sayılar:")
for i in range(1, 101):
    print(i, end=" ")  # Sayıları yan yana yazdırır

print("\n" + "-"*50)  # Ayırıcı çizgi


# 📌 2. 1'den 100'e kadar olan sadece çift sayıları yazdıran program
print("1’den 100’e kadar olan çift sayılar:")
for i in range(2, 101, 2):  # 2'şer artarak gider
    print(i, end=" ")

print("\n" + "-"*50)


# 📌 3. Kullanıcının girdiği bir sayının faktöriyelini hesaplayan program
def faktoriyel_hesapla(n):
    faktoriyel = 1
    for i in range(1, n + 1):
        faktoriyel *= i
    return faktoriyel

sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz!")
else:
    print(f"{sayi}! = {faktoriyel_hesapla(sayi)}")

print("\n" + "-"*50)


# 📌 4. 1'den 100'e kadar olan asal sayıları bulan program
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):  # 2'den kareköküne kadar bölme kontrolü
        if sayi % i == 0:
            return False
    return True

print("1’den 100’e kadar olan asal sayılar:")
for i in range(1, 101):
    if asal_mi(i):
        print(i, end=" ")

print("\n" + "-"*50)