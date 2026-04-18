import pandas as pd
import numpy as np
banklar = []
Bank = {"Bank haqida Parol kirtasiz va ism kirtasiz"}
print(Bank)
qoshilish = ("Pastagi yerdan ro'yxatdan oting",)
print(qoshilish)
#qoshish funksyiyasi
def qosh():
    ism = input("Ism :")
    parol = int(input("Parol (faqat son) :"))
    balans = int(input("Balans :"))
    royxat = {"Ism": ism, "parol":parol, "balans":balans}
    banklar.append(royxat)
#login funksiyasi
def login():
    ism_k = input("Ism :")
    parol_k = int(input("Parol :"))
    topildi = False
    for foydalanuvchi in banklar:
        if foydalanuvchi['Ism'] == ism_k:
            topildi = True
            if foydalanuvchi['parol'] == parol_k:
                print(f"Parol to'gri balansingiz : {foydalanuvchi['balans']}")
            else:
                print("Parol xato!")
                return
            if not topildi:
                print("Bunday foydalanuvchi topilmadi!")
#korish funksyiasi
def korish(data):
    if not data:
        print("Hozircha balans yo'q!")
        return
    for b in banklar:
        print(f"Ism: {b['Ism']}, {b['parol']}, {b['balans']}")
#eng kop balans
def qimmat(data):
    if not data:
        print(f"Hozircha balans yo'q!")
        return
    eng = max(data, key=lambda x: x['balans'])
    print(f"Eng qimmat Balans egasi :{eng['Ism']} balabsi :{eng['balans']}")
#ortacha balans funksiyasi
if banklar:
    df = pd.DataFrame(banklar)
    ortacha = np.mean(df[['Ism', 'parol', 'balans']])
    print(f"O'rtacha Balans :{ortacha}")
#Ozgartirish funksiyasi
    df = df.set_axis(['Ism', 'parol', 'balans'], axis=1)
    print(df)
    df['balans'] = df['balans'] + 5000
# numpy array
    arr = np.array([
        'alisher usmonov', 1400000000,
        'Jahongiz ortiqhojayev', 800000000,
        'Gulnora Karimova', 600000000,
    ])
    print(f"Bizga kiredt qoygan mashxur inson :{arr[1]}")
    print(f"Siz balansingizga 5000 so'm qoshildi {df['balans']}")
#wile true orqali menyu
while True:
    print("1. Royxatdan o'tish")
    print("2. Login")
    print("3. Balansni ko'rish")
    print("4. Eng qimmat balans")
    print("5. O'rtacha balans")
    print("6. CHiqish")
    tanlov = int(input("Tanlov :"))
#if elif else orqali tanlov
    if tanlov == 1:
        qosh()
    elif tanlov == 2:
        login()
    elif tanlov == 3:
        korish(banklar)
    elif tanlov == 4:
        qimmat(banklar)
    elif tanlov == 5:
        if banklar:
            df = pd.DataFrame(banklar)
            ortacha = np.mean(df['balans'])
            arr = np.array([
        'alisher usmonov', 1400000000,
        'Jahongiz ortiqhojayev', 800000000,
        'Gulnora Karimova', 600000000,
    ])
            print(f"O'rtacha Balans :{ortacha}")
            print(f"Bizga kiredt qoygan mashxur inson :{arr[1]}")
            df['balans'] = df['balans'] + 5000
            print(f"Siz balansingizga 5000 so'm qoshildi {df['balans']}")
            print(df['balans'])
        else:
            print("Hozircha balans yo'q!")
    elif tanlov == 6:
        print("Dasturdan chiqildi!")
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring!")

