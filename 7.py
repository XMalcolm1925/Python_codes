"""
Quyidagi mashqlarni bajaring:

    1.ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
"""
ismlar = ["Ahmad", "Ali", "Vali", "Siddiq"]

print("Assalomu alaykum ", ismlar[0], ". Salomatmisiz?")
print(ismlar[1], " yaxshimisiz? \n Ahvollar qalay?")
print(ismlar[2], ", bugun ", ismlar[3], "bilan to'rtalamiz mehmonga chaqirilganmiz!")

print("*" * 10)
# ***********
"""    2.sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
"""
sonlar = [25, 21, 47, 1.2, -1, 30]

print(sonlar[1] * sonlar[3] + sonlar[0] + (sonlar[2] - sonlar[-1]))

sonlar[0] = 30
sonlar[-1] = 43
sonlar[5] = sonlar[5] - 10
print(sonlar[5] * sonlar[0] - sonlar[-1])
"""    3.t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating 
biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, 
ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib oling (.pop()).
"""
sahobalar = ["Abu Bakr", "Umar", "Usmon", "Aliy"]
imomlar = ["Buxoriy", "Muslim", "Molik", "Ahmad"]

sahoba = sahobalar.pop(0)
imom = imomlar.pop(0)

print(f"Sahobalar ichida {sahoba} 'Siddiq' degan nom olgan")
print(f"imomlardan {imom} eng sahih hadis to'plamini yozishga musharraf bo'lgan")
"""    4.friends nomli bo'sh ro'yxat tuzing va unga 
.append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
"""
friends = []

friends.append("Abu Bakr")
friends.append("Umar")
friends.append("Usmon")
friends.append("Aliy")
friends.append("Molik")
friends.append("Ahmad")

print(f"Bugun do'stlarim {friends}larni mehmonga chaqirgandim. ")

friends.pop(1)
friends.pop(2)

print(f"lekin {friends}lar keldi, qolganlar yo'q. ")

friends.insert(0, "Aminjon")
friends.insert(4, "Rustam")

print(
    f"Kelmagan do'stlarimni o'rniga qo'shnilarimni taklif qildim, natijada mehmonlar {friends} bo'ldi. "
)

"""    5.Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. 
.pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini 
friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
"""
mehmonlar = []

friends.pop(1)
friends.pop(2)
friends.pop(3)

mehmonlar.append("Abu Bakr")
mehmonlar.append("Umar")
mehmonlar.append("Usmon")
mehmonlar.append("Aliy")
mehmonlar.append("Molik")
mehmonlar.append("Ahmad")

print(mehmonlar)
