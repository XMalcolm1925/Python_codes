"""
1) Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", 
agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
"""
# 1
# son = int(input("Juft son kiriting: "))

# if son % 2 == 0:
#     print("Rahmat! ")
# else:
#     print("Bu son juft emas! ")

"""
Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
"""
# 2
# yosh = int(input("Yoshingizni kiriting!: "))

# narx1 = "10000"
# narx2 = "20000"
# narx3 = "tekin"

# if yosh >= 5 and yosh <= 17:
#     print(narx1)
# elif yosh >= 18 and yosh <= 59:
#     print(narx2)
# else:
#     print(narx3)
# ============================
# if yosh <= 4 or yosh >= 60:
#     print(narx3)
# elif yosh < 18:
#     print(narx1)
# else:
#     print(narx2)
"""
Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring 
va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
"""
# 3
# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))

# if son1 > son2:
#     print(f"{son1} > {son2} Birinchi son katta! ")
# elif son1 < son2:
#     print(f"{son1} < {son2} Ikkinchi son katta! ")
# else:
#     print(f"{son1} = {son2} Ikkala son teng! ")
"""
mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
"Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
"""
# 4
# mahsulotlar = [
#     "sut",
#     "qatiq",
#     "non",
#     "uzum",
#     "olma",
#     "asal",
#     "pishloq",
#     "suv",
#     "anor",
#     "choy",
#     "novot",
# ]
# savat = []

# while len(savat) != 5:
#     mahsulot = input("Mahsulot tanlang!: ")

#     if mahsulot.lower() in mahsulotlar:
#         savat.append(mahsulot)
#         print(f"Albatta, {mahsulot} do'konimizda bor")
#     else:
#         print(f"Kechirasiz! {mahsulot} do'konimizda yo'q")
# print(f"siz olgan mahsulotlar: {savat}")
# ======================================
# for i in range(5):
#     savat.append(input(f"Savatga {i+1}-mahsulotni qo'ying: "))

# for i in savat:
#     if i in mahsulotlar:
#         print(f"Do'konimizda {i} bor! ")
#     else:
#         print(f"Do'konimizda {i} yo'q! ")
"""
Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi bor_mahsulotlar degan ro'yxatga, 
do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. 
Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, 
aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
"""
mahsulotlar = [
    "sut",
    "qatiq",
    "non",
    "uzum",
    "olma",
    "asal",
    "pishloq",
    "suv",
    "anor",
    "choy",
    "novot",
]
# bor_mahsulotlar = []
# mavjud_emas = []

# while len(bor_mahsulotlar + mavjud_emas) != 5:
#     mahsulot = input("Mahsulot tanlang!: ")

#     if mahsulot.lower() in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#         print(f"Albatta, {mahsulot} do'konimizda bor")
#     else:
#         mavjud_emas.append(mahsulot)
#         print(f"Kechirasiz! {mahsulot} do'konimizda yo'q")
# print(f"Do'konimizda bor mahsulotlar: {bor_mahsulotlar}")
# print(f"Do'konimizda yo'q mahsulotlar: {mavjud_emas}")
# =================================
# savat = []
# for i in range(5):
#     savat.append(input(f"Savatga {i+1}-mahsulotni qo'ying!: "))
# bor_mahsulotlar = []
# yoq_mahsulotlar = []
# for i in savat:
#     if i in mahsulotlar:
#         bor_mahsulotlar.append(i)
#     else:
#         yoq_mahsulotlar.append(i)

# if yoq_mahsulotlar:
#     print("Do'knimizda quyidagi mahsulotlar yo'q:")
#     for i in yoq_mahsulotlar:
#         print(i)
# else:
#     print("Siz so'ragan barcha mahsulot do'konimizda bor! ")
"""
foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni 
foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
"""
# foydalanuvchilar = ["anvar12", "saad_Alloh1", "janob_h", "Jaa_surBUK", "qashqirJON"]
# login = input("login kiriting: ")

# if login.lower() not in foydalanuvchilar:
#     print(f"XUSH KELIBSIZ!: {login}")
# else:
#     print(f"'{login}' BAND! BOSHQA LOGIN TANLANG! ")

("""
Foydalanuvchidan biror butun son kiritishni so'rang. 
Foydalanuvchi kiritgan sonni 2 dan 10 gacha bo'lgan sonlardan qay biriga 
qoldiqsiz bo'linishini konsolga chiqaring.
""")
# son = int(input("butun son kiriting: "))
# if son % 2 == 0:
#     print(f"{son} % 2 = {son % 2}")
# elif son % 3 == 0:
#     print(f"{son} % 3 = {son % 3}")
# elif son % 4 == 0:
#     print(f"{son} % 4 = {son % 4}")
# elif son % 5 == 0:
#     print(f"{son} % 5 = {son % 5}")
# elif son % 6 == 0:
#     print(f"{son} % 6 = {son % 6}")
# elif son % 7 == 0:
#     print(f"{son} % 7 = {son % 7}")
# elif son % 8 == 0:
#     print(f"{son} % 8 = {son % 8}")
# elif son % 9 == 0:
#     print(f"{son} % 9 = {son % 9}")
# elif son % 10 == 0:
#     print(f"{son} % 10 = {son % 10}")
# else:
#     print("butun son kiriting, o'nli son bo'lmasin! ")
# ==================================
son = int(input("butin son kiriting: "))

for i in range(2, 11):
    if son % i == 0:
        print(
            f"""
              ({son} % {i} = {son%i}) 
              {son} soni {i} ga qoldiqsiz bo'linadi!
              """
        )
    else:
        print(
            f"""
                {son} % {i} = {son%i}
                """
        )
