import numpy as np
import pandas as pd
mahsulotlar = []
#Aqli magazin haqida
print('==========SMART SHOP SYSTEM==========')
haqida = ("Aqli dastur haqida bunda mahsulot qoshasiz va korsangiz ham boladi mahsulotni")
print(haqida)
#hozircha bor mahsulotlar
se = {"Avvalgi narx",}
print(se)
raw = np.array([
    ['Coca cola',8000],
    ['Non',4000],
])
df = pd.DataFrame(raw)
df = df.set_axis(['Mahsulot', 'Narxi'],axis=1)
print(df)
df['Narxi'] = df['Narxi'].astype(int)
df['Narxi'] = df['Narxi'] - 500
print(f"Hozir magazinda bor ichimliklar:", raw[0] )
print(df)
print("Hozirgi narx")
df = df.set_index("Mahsulot")
print(df.loc[['Non', 'Coca cola']])
#Mahsulot qo'shish funksiyasi
def qosh():
    nomi = input("Mahsulot nomi :")
    narxi = int(input("Narxi :"))
    soni = int(input("Soni :"))
    kotegor = input("Kotegoryasi :")
    mahsulot = {'Nomi': nomi, 'Narxi': narxi, 'Soni': soni, 'Kotegoryasi': kotegor}
    mahsulotlar.append(mahsulot)
    print(f"Mahsulot {nomi} qo'shildi")
#Ko'rish funksiyasi
def korish(data):
    if not data:
        print("Savat bo'sh")
        return
    for m in mahsulotlar:
        print({'Nomi': m['Nomi'], 'Narxi': m['Narxi'], 'Soni': m['Soni'], 'Kotegoryasi': m['Kotegoryasi']})
#qidirish funksiyasi
def qidir():
    nom_k = input("Mahsulot nomi :")
    topildi = False
    for foydalanuvchi in mahsulotlar:
        if foydalanuvchi['Nomi'] == nom_k:
            topildi = True
            narxi = foydalanuvchi['Narxi']
            soni = foydalanuvchi['Soni']
            kateg = foydalanuvchi['Kotegoryasi']
            print(f"Mahsulot topildi! Narxi: {narxi}, Soni: {soni}, Kategoriyasi: {kateg}")
            break 
    if not topildi:
        print("Bunday mahsulot topilmadi !")
#mahsulot yangilash funksiyasi
def yangilash():
    nom_k = input("Mahsulot nomi :")
    topildi = False
    for m in mahsulotlar:
        if m['Nomi'] == nom_k:
            topildi = True
            angi_narx = int(input(f"{nom_k} uchun yangi narx: "))
            yangi_soni = int(input(f"{nom_k} uchun yangi soni: "))
            m['Narxi'] = angi_narx
            m['Soni'] = yangi_soni
            print(f"Muvaffaqiyatli yangilandi: {nom_k}")
            break # Topilgach, siklni to'xtatamiz
    if not topildi:
        print("Bunday mahsulot topilmadi!")
#sotuv funksiyasi
def sotuv():
    nom = input("Mahsulot nomi :")
    topildi = False
    for m in mahsulotlar:
        if m['Nomi'] == nom:
            topildi = True
            nechta = int(input(f"Nechta {nom} sotib olasiz :"))
            if nechta < m['Soni']:
                jami = m['Narxi'] * nechta
                m['Soni'] -= nechta
            print(f"Sotuv bajarildi!")
            print(f"Jami summa: {jami} so'm")
            print(f"Omborda qoldi: {m['Soni']} ta")
        else:
            print(f"Xato! Omborda bor-yog'i {m['Soni']} ta mahsulot bor.")
            break    
    if not topildi:
        print("Kechirasiz, bunday mahsulot bizda yo'q.")
#eng qimmat tavarni korish
def qimmat(data):
    if not data:
        print("Savat bo'sh")
        return
    eng = max(data, key=lambda x:x['Narxi'])
    return f"Eng qimmat mahsulot narxi {eng['Nomi']}, Narxi: {eng['Narxi']} so'm"
#statistikani korish
def ststis(data):
    if not data:
        print("statistika uchun ma'lumot yetarli emas")
        return
    temp_df = pd.DataFrame(data)
    ortacha = np.mean(temp_df['Narxi'])
    jami = np.sum(temp_df['Soni'])
    print("========DO'KON STATISTIKA========")
    print(f"Ombrdagi jami mahsulot soni: {jami}")
    print(f"Mahsulotlarni o'rtacha narxi: {ortacha}")
    print("=================================")
#loop funksiyasi
while True:
#dastur qoidasi
    print("1 Mahsulot qoshish")
    print("2 Mahsulot ko'rish")
    print("3 qidirish")
    print("4 yangilash")
    print("5 sotuv qilish")
    print("6 eng qimmat mahsulot ko'rish")
    print("7 statistika")
    print("8 chiqish")
    tanlov = int(input("Tanlov :"))
    if tanlov == 1:
        qosh()
    elif tanlov == 2:
        korish(mahsulotlar)
    elif tanlov == 3:
        qidir()
    elif tanlov == 4:
        yangilash()
    elif tanlov == 5: 
        sotuv()
    elif tanlov == 6:
        qimmat(mahsulotlar)
    elif tanlov == 7:
        ststis(mahsulotlar)
    elif tanlov == 8:
        print("Dasturdan chiqildi xayr")
        break
    else:
        print("Xato son kiriting!")
#csvga saqalash
    df.to_csv('talaba.csv', index=False)

