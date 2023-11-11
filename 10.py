"""
1.    Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
      ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
      GM uchun ikkala harfni katta qiling.
2.    Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
3.    Foydalanuvchidan login ismini so'rang. 
      Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini chiqaring. 
      Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
4.    Foydalanuvchidan 2 ta son kiritishni so'rang. 
      Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni chiqaring.
5.    Foydalanuvchidan istalgan son kiritishni so'rang. 
      Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
6.    Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
      Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
"""
#1
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(f"{car.upper()}")
    else:
        print(f"{car.title()}")

# print(cars.upper()) if cars == 'gm' else print(cars.title())

#2
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(f"{car.title()}")
    else:
        print(f"{car.upper()}")

# print(cars.title()) if cars != 'gm' else print(cars.upper())

#3
login = input("login kiriting:\n ")
if login == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}")

# print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?") if login == 'admin' else print(f"Xush kelibsiz, {login}")

#4
son  = int(input("birinchi sonni kiring: "))
son_ = int(input("ikkinchi sonni kiring: "))
# if son == son_:
#     print("sonlar teng ekan! ")

if son == son_ : print("sonlar teng ekan! ") 

#5
istalganSon = int(input("istalgan bir son kiriting: "))
# if istalganSon < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

print("Manfiy son") if istalganSon < 0 else print("Musbat son")

#6
number = int(input("Musbat son kiriting: "))
# if number > 0:
#     print(number**(1/2))
# else:
#     print("Musbat son kiring!")

print(number**(1/2)) if number > 0 else print("Musbat son kiritng!")