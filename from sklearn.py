import numpy as np
import pandas as pd
#list oyinchilarni saqlash uchun
oyinchilar = []
stats = np.array([
    [92,91,88]
])
gol = ([
    [33,22],
    [32,20],
    [30,15]
])
macsum = ([
    [[34,22,19], [39,33,11]],#pele
    [[30,18,9], [37,35,13]],#marodona
    [[29,22,5], [34,27,13]] #cruft
])
print(f"Pele marodona cruft 2 mavsumdagi natijalari:", macsum)
mas = np.sum(macsum, axis=2)
print(f"Jami mavsum gol assist pele : {mas[0]}")
print(f"Jami mavsum gol assist marodona :{mas[1]}")
print(f"Jami mavsum gol assist cruft :{mas[2]}")
print(stats)
print(f"O'yinchilarni 1 pele 2 marodona 2 cruft goli va assitsi jami natija : {np.sum(gol,axis=1)}")
ortacha = np.mean(stats, axis=0)
oyin = ("Top 6 old o'yinchilar", "1 pele", "2 marodona", "3 cruft",)
mask = ortacha - stats
print(f"top 3 ta oyinchilar reyting farqi : {mask}")
oyin2 = {"pastdagi ro'yxatni tanlang va qo'shiling",}
print(oyin)
print(oyin2)
#oyinchi qoshish funksiyasi
def qoshish():
    ism = input("O'yinchi ismi Kiriting :")
    gol = int(input("O'yinchi gol soni :"))
    assist = int(input("O'yinchi assist soni :"))
    oyin = int(input("O'yin soni :"))
#oyinchi haqida ma'lumotlarni lug'atga saqlash
    oyichi = {
        'ism': ism,
        'gol': gol,
        'assist': assist,
        'oyin': oyin
    }
    oyinchilar.append(oyichi)
#oyinchi korish funksiyasi
def korsat(data):
    if not data:
        print("Hozircha o'yinchilar yo'q")
        return
    for o in oyinchilar:
        gol = np.array([o['gol']for o in data])
        asist = np.array([o['assist']for o in data])
        oyin = np.array([o['oyin']for o in data])
        qosh = gol[gol > 22] + 2
        print(f"O'yinchilarga 22 dan kop gol urganlarga 2 ta gol qo'shish : {qosh}")
        samaradorlik = (qosh + asist) / oyin
#oyinchi haqida ma'lumotlarni chiqarish
        print('--------------------------------------------')
        print(f"O'yinchi ismi : {o['ism']}")
        print(f"Gol soni : {o['gol']}")
        print(f"Assist soni : {o['assist']}")
        print(f"O'yin soni : {o['oyin']}")
        print(f"Samaradorlik : {samaradorlik}")
        print('--------------------------------------------')
    gollar = np.array([o['gol']for o in data])
    kam = np.argmin(gollar)
    print(f"Eng kam gol urgan o'yinchi : {data[kam]['ism']} , Gol soni : {data[kam]['gol']}")
#indexing slicing yordamida gol sonini chiqarisg
    gollar = np.array(oyinchilar)
    toq = gollar[::-1]
    print(f"Barcha gollar :{gollar}")
    print(f"1 chi gol : {toq}")
#kop gol urgan o'yinchini chiqarish
def kop_gol(data):
    if not data:
        print("Hozircha o'yinchilar yo'q")
        return
    kop = max(data, key=lambda x: x['gol'])
#kop gol urgan o'yinchi haqida ma'lumotlarni chiqarish
    print('--------------------------------------------')
    print(f"Eng kop gol urgan o'yinchi : {kop['ism']}")
    print(f"Gol soni : {kop['gol']}")
    print('--------------------------------------------')
#oyinchi ochirish funksiyasi
def ochirish(data):
    if not data:
        print("Hozircha o'yinchilar yo'q")
        return
#oyinchi haqida ma'lumotlarni o'chirish
    ism = input("O'chirish uchun o'yinchi ismi :")
    gol = int(input("O'chirish uchun o'yinchi gol soni :"))
    for o in data:
        if o['ism'] == ism and o['gol'] == gol:
            data.remove(o)
            print(f"{ism} o'yinchisi o'chirildi")
            return
        print(f"{ism} o'yinchisi topilmadi")
#asosiy dastur
while True:
    print("1. O'yinchi qo'shish")
    print("2. O'yinchilarni ko'rsatish")
    print("3. Eng kop gol urgan o'yinchini ko'rsatish")
    print("4. O'ychini o'chirish")
    print("5. Chiqish")
    tanlov = input("Tanlovni kiriting :")
#if elif else opertorlari yordamida tanlovni amalga oshirish
    if tanlov == '1':
        qoshish()
    elif tanlov == '2':
        korsat(oyinchilar)
    elif tanlov == '3':
        kop_gol(oyinchilar)
    elif tanlov == '4':
        ochirish(oyinchilar)
    elif tanlov == '5':
        if oyinchilar:
            df = pd.DataFrame(oyinchilar)
            df.to_csv('talaba.csv')
            print("Ma'lumot talaba.csv ga saqlandi!")
        print("DAsturdan chiqildi")
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring")




 
