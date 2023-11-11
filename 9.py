"""
1.  Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
2.  Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring 
    (n o'rniga kod necha marta takrorlanganini yozing)
3.  10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
4.  Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
5.  Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
    va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. 
    Ro'yxatni konsolga chiqaring.
"""
#1
ismlar = ["Anvar","Sarvar","Jasur","Ali","Shokir"]
for ism in ismlar:
    print(f"Salom,{ism} \nYaxshimisiz?")
#2
print(f"Kod {len(ismlar)} marta takrorlandi")
#3
sonlar = list(range(11,100,2))
for son in sonlar:
    print(f"{son}ning kubi {son**3}ga teng")
#4
kinolar = []
for s in range(1,6):
    kinolar.append(input(f"{s}-sevimli kinongizni nomini kiring!: "))
print(kinolar)
#5
arkadash = int(input("Bugun nechta do'stingiz bilan ko'rishtingiz?: "))
suhbatdoshlar = []
for s in range(arkadash):
    suhbatdoshlar.append(input(f"{s+1}-so'hbatdoshingizning ismi nima?: "))
    print(s)
print(suhbatdoshlar)