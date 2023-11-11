"""Foydalanuvchidan ikki son kiritshni so'rab, 
Kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur"""

print("Ikkita son kiriting, men sizga bu sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini hisoblab beraman! ")
son  = int(input("Birinchi sonni kiriting!: "))
son_ = int(input("Ikkinchi sonni kiriting!: "))
SON1 = son + son_
SON2 = son - son_
SON3 = son * son_
SON4 = son / son_
print(F"""
{son} + {son_} = {SON1}
{son} - {son_} = {SON2}
{son} * {son_} = {SON3}
{son} / {son_} = {SON4}
""")