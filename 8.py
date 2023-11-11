"""
1.  O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
2.  Ro'yxatning uzunligini konsolga chiqaring
3.  sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
4.  sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
5.  Asl ro'yxatni qaytadan konsolga chiqaring
6.  reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
7.  sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
8.  120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
9.  Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
10. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
11. Ro'yxatdagi elementlar sonini hisoblang
12. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
13. taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
14. nonushta degan yangi ro'yxatga taomlardan nusxa oling
15. Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
16. Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
17. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
"""
#1
davlatlar = ["O'zbekiston", "Turkiya", "Misr", "rossiya", "xitoy"]
print(davlatlar)
#2
uzunlik = len(davlatlar)
print(F"ro'yxatning uzuligi: {uzunlik}")
#3

print(F"ro'yxatning tartibli shakli: {sorted(davlatlar)}")
#4

print(F"ro'yxatning teskari tartibli shakli: {sorted(davlatlar,reverse=True)}")
#5
asl_royxat = davlatlar
print(f"asl ro'yxat: {asl_royxat}")
#6
asl_royxat.reverse()
print(f"reverse yordamida ro'yxatning teskari shakli: {asl_royxat}")
#7
asl_royxat.sort()
print(f"sort yordamida ro'yxatni alifbo bo'yicha tartibi: {asl_royxat}")
asl_royxat.sort(reverse=True)
print(f"sort yordamida ro'yxatni alifboga teskari tartibi: {asl_royxat}")
#8
juft_sonlar = list(range(120,1200,2))
#9
yigindi = sum(juft_sonlar)
print(F"juft_sonlar listidagi barcha sonlarning yig'indisi: {yigindi}")
#10
engKatta = max(juft_sonlar)
engKichik = min(juft_sonlar)
ayirma = engKatta - engKichik
print(F"juft_sonlar listidagi eng katta sondan eng kichik sonning ayirmasi: {ayirma}")
#11
raqamlarSoni = len(juft_sonlar)
print(F"juft_sonlar listida {raqamlarSoni} ta son bor!")
#12
print(f"""
boshidagi yettita son {juft_sonlar[:7]},
o'rtasidagi yettita son{juft_sonlar[300:307]},
oxiridagi yettita son{juft_sonlar[533:]}.
""")
#13
taomlar = ["palov","manti","somsa","menemen","lag'mon"]

#14
nonushta = taomlar[:]
#15
nonushta.append("qovurilgan tuxum")
nonushta.append("shirguruch")
nonushta.remove("manti")
nonushta.remove("somsa")
#16
print(taomlar)
print(nonushta)
#17
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non" 
#TypeError: 'tuple' object does not support item assignment