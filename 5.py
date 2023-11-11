"""Quyidagi mashqlarni bajaring:

Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
1.Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
2.Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
3.Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
4.Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
5.manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
"""
#1
kocha = "bog'bon"
mahalla = "sog'bon"
tuman = "BODOMZOR"
viloyat = "SAMARQAND"
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati. ")
#2
kocha = input("qaysi ko'chada yashaysiz? ")
mahalla = input("qaysi mahallada yashaysiz? ")
tuman = input("qaysi tumanda yashaysiz? ")
viloyat = input("qaysi viloyatda yashaysiz? ")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati. ")
#3
print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati.")
#4
yangi_manzil = f"{kocha} ko'chasi,{mahalla} mahallasi,{tuman} tumani,{viloyat} viloyati."
print(yangi_manzil)
#5
yangi_manzil_ = f"{kocha.upper()} ko'chasi,{mahalla.title()} mahallasi,{tuman.lower()} tumani,{viloyat.capitalize()} viloyati."
print(yangi_manzil_)
