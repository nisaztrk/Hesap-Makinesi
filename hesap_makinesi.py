# Toplama, çıkarma, çarpma, bölme ve üs alma gibi basit işlemlerin yapılabildiği temel bir hesap makinesi
import math

def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y

def carpma(x,y):
    return x*y

def bol(x,y):
    return x/y

def us(x,y):
    return x**y


def kok(x,y):
    return x**(1/y)

# 10 tabanında logaritma alma x=sayı y=taban

def logaritma(x, y):
    return math.log(x, y)


    
print("Lütfen yapmak istediğiniz işlemi seçiniz.")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
print("5. Üs alma")
print("6. Kökünü Alma")
print("7. Logaritma Alma")

secim= input("Seçiminiz (1/2/3/4/5/6/7): ")
sayi1= float(input("İlk sayıyı girin: "))
sayi2= float(input("İkinci sayıyı girin: "))

if secim =="1":
    print(sayi1,"+",sayi2,"=" , topla(sayi1,sayi2) )

elif secim =="2":
    print(sayi1, "-", sayi2, "=", cikar(sayi1,sayi2))

elif secim == "3":
    print(sayi1, "*" , sayi2, "=", carpma(sayi1, sayi2) )

elif secim == "4":
    if sayi2==0:
        print("Bir sayı sıfıra bölünemez")
    else:
        print(sayi1, "/" , sayi2, "=", bol(sayi1,sayi2))

elif secim == "5":
    print(sayi1,"**",sayi2,"=" , us(sayi1,sayi2) )

elif secim== "6":
    print(sayi1,"**","(1/",sayi2,")", "==",  kok(sayi1, sayi2) )

elif secim=="7":
    print("log",sayi1, "taban: ",sayi2 , "=", logaritma(sayi1, sayi2))
    


else:
    print("Geçersiz seçim.")










