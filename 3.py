"""
Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:

"Nexia", "Tico", 'Damas' ko'rganlar qilar havas

Quyidagi misollarga yechimni Pythonda chiqaring. 
Har bir misoldan avval misol matnini izoh ko'rinishida yozing:

5 ning 4-darajasini toping
22 ni 4 ga bo'lganda qancha qoldiq qoladi?
Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
Diametri 12 ga teng bo'lgan doiraning yuzini toping 
(π=3.14 deb oling)
Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping 
(Pifagor teoremasidan foydalaning)
"""
print("\"Nwxia\", \"Tico\",\"amas\" ko'rganlar qilar havas")

print("5 ning 4-darajasini toping")

print(5**4)

print("22 ni 4 ga bo'lganda qancha qoldiq qoladi?")

print(22%4)

print("Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping")

print(125**2)
print(125*4)

print("""
Diametri 12 ga teng bo'lgan doiraning yuzini toping 
(π=3.14 deb oling)
""")
      
print(3.14*(12/2)**2)

print("""
Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping 
(Pifagor teoremasidan foydalaning:(c*c)=(a*a)+(b*b))
a=6
b=7
c=(a**2+b**2)**(1/2)
""")

a=6
b=7
c=(a**2+b**2)**(1/2)
print(c)