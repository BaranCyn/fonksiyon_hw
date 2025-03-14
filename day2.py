
faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

# Tip dönüşümleri
print(int(vade) + 12)

faiz = str(faiz)
print(type(faiz))

# Kullanıcıdan veri alma
try:
    vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))
    print(type(vade))
    vade = vade + 12
except ValueError:
    print("Geçersiz giriş! Lütfen sadece sayı giriniz.")

print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

# String formatlama
isim = "Baran"
metin = f"Merhaba {isim}"
print(metin)

# Listeler
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(len(krediler[0]))

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop()
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Z Kredisi"])  # extend içine liste verildi
print(krediler)

# Döngüler
for i in range(10):
    print(i)

for i in range(5,10):
    print(i)

for i in range(0,51,10):
    print(i)

# Fonksiyonlar
def calculate():
    print(100 - 20)

def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Batu")
sayHello("Baran")

def calculateAndReturn(price, discount):
    return price - discount

print("************")
fonk1 = calculateAndReturn(100,50)
fonk2 = calculateAndReturn(300,100)
print(fonk1)
print(fonk2)
print("**********")





    



