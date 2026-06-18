import streamlit as st
import pandas as pd
st.title("SMART SHOP SYSTEM")
if 'mahsulotlar' not in st.session_state:
    st.session_state.mahsulotlar = []
with st.sidebar:
    tanlov = st.radio("Amalni tanlang:", ['Qoshish', 'Korish', 'Qidirish', 'Sotuv', 'Xarita'])
if tanlov == 'Qoshish':
    st.subheader("Yangi mahsulot qo'shish")
    with st.form("qoshish_formi"):
        nomi = st.text_input("Nomi:")
        narxi = st.number_input("Narxi:", min_value=0)
        soni = st.number_input("Soni:", min_value=1)
        kateg = st.text_input("Kotegoryasi:")
        submit = st.form_submit_button("Qo'shish")
        if submit:
            yangi = {'Nomi': nomi, 'Narxi': narxi, 'Soni': soni, 'Kategoryasi': kateg}
            st.session_state.mahsulotlar.append(yangi)
elif tanlov == "Korish":
    st.subheader("Mahsulotlar ro'yxati")
    if not st.session_state.mahsulotlar:
        st.write("Savat bo'sh")
    else:
        st.table(st.session_state.mahsulotlar)
elif tanlov == "Qidirish":
    st.subheader("Mahsulot qidirish")
    nom_k = st.text_input("Qidirilayotgan mahsulot nomi:")
    if nom_k:
        topildi = [m for m in st.session_state.mahsulotlar if m['Nomi'].lower() == nom_k.lower()]
        if topildi:
            st.write(topildi[0])
        else:
            st.error("Topilmadi!")
elif tanlov == "Sotuv":
    st.subheader("Sotuv qilish")
    if not st.session_state.mahsulotlar:
        st.write("Omborda mahsulot yoq")
    else:
        nomlar = [m['Nomi'] for m in st.session_state.mahsulotlar]
        sotuv_n = st.selectbox("Mahsulotni tanlang:", nomlar)
        nechta = st.number_input("Nechta sotib olasiz:", min_value=1)
        if st.button("Sotish"):
            for m in st.session_state.mahsulotlar:
                if m['Nomi'] == sotuv_n:
                    if m['Soni'] > nechta:
                        m['Soni'] -= nechta
                        st.success(f"Sotildi! Jami: {m['Narxi'] * nechta} so'm")
                    else:
                        st.error("Omborda yetarli emas!")
elif tanlov == 'Xarita':
   st.title("Xorazm (Urganch)Sherzod do'kon xaritasi")
   xorazm_manzil = pd.DataFrame({
        'lat': [41.5501],
         'lon': [60.6313]
         })
   st.map(xorazm_manzil)



print("Coffe and bakery")
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression

# Sarlavha (To'plam emas, oddiy matn qilindi)
print("=== SMART COFFE AND BAKKERY ===")

# Pandas qismi (Sintaktik xatolar tuzatildi)
df = pd.DataFrame({
    "Id":,
    "Coffe_x": ["Latte", np.nan]
})

df1 = pd.DataFrame({
    "Id":,
    "Coffe_y": [np.nan, "Coffe"]
})

df2 = pd.merge(df, df1, on="Id", how='outer')
print("\n--- Birlashgan ma'lumotlar jadvali ---")
print(df2)

print("\n===== HOZIRDA MAVJUD BO'LMAGAN MAHSULOTLAR TO'LDIRILDI =====")
df2.fillna({
    "Coffe_x": "Americano",
    "Coffe_y": "Capuccino"
}, inplace=True)
print(df2)
print("==========================================================\n")

# Global ro'yxat
mahsulotlar = []

def qosh():
    nomi = input("Mahsulot nomi: ")
    narxi = float(input("Mahsulotga kerakli narxni kiriting (so'm): "))
    soni = int(input("Nechta mahsulot bor: "))
    # TUZATILDI: Set o'rniga haqiqiy Dictionary (lug'at) yaratildi
    mahsulot = {
        "Nomi": nomi,
        "Narxi": narxi,
        "Soni": soni
    }
    mahsulotlar.append(mahsulot)
    print("✅ Mahsulot muvaffaqiyatli qo'shildi!\n")

def menyu(data):
    if not data:
        print("⚠️ Menyuda biror narsa mavjud emas\n")
        return
    
    print("\n================= MENYU =================")
    for m in data:  # TUZATILDI: global emas, kelgan data ishlatildi
        print(f"Nomi: {m['Nomi']} | Narxi: {m['Narxi']} so'm | Qoldiq: {m['Soni']} ta")
    print("=========================================\n")

def Buyurtma(data):
    if not data:
        print("⚠️ Mahsulotlar mavjud emas\n")
        return
    
    print("\n=========== BUYURTMA BERISH ===========")
    mahsulot_nomi = input("Mahsulot nomi: ")
    son = int(input("Soni: "))

    # Mahsulotni qidirib topish
    topilgan_mahsulot = next((m for m in data if m['Nomi'].lower() == mahsulot_nomi.lower()), None)

    if topilgan_mahsulot:
        if topilgan_mahsulot['Soni'] >= son:
            narx = son * topilgan_mahsulot['Narxi']
            print(f"✅ {son} ta {topilgan_mahsulot['Nomi']} sotildi. Jami narx: {narx} so'm")
            
            # TUZATILDI: Qiymatni kamaytirish va saqlash to'g'rilandi (=)
            topilgan_mahsulot['Soni'] -= son
            print(f"Ombordagi qoldiq soni: {topilgan_mahsulot['Soni']} ta")
        else:
            print(f"❌ Omborda yetarli mahsulot yo'q! Hozirda {topilgan_mahsulot['Soni']} ta bor.")
    else:
        print("❌ Mahsulot topilmadi!")
    print("=======================================\n")

def tarxi(data):
    if not data:
        print("⚠️ Hozircha mahsulotlar kiritilmagan\n")
        return
    
    print("\n========= BUYURTMALAR TARIXI =========")
    for m in data:
        print(f"Nomi: {m['Nomi']} | Narxi: {m['Narxi']} so'm | Hozirgi qoldiq: {m['Soni']} ta")
    print("======================================\n")

def ombor():
    print("\n========== OMBOR MONITORINGI ==========")
    sut = int(input("Sut miqdori (litrda): "))
    coffe = int(input("Coffee Beans (kg da): "))
    sugar = int(input("Shakar (kg da): "))

    if sut < 8:
        print("⚠️ Sut kam qoldi!")
    else:
        print("Sut: Hali yetarli ✅")

    if coffe < 4:
        print("⚠️ Coffee beans kam qoldi!")
    else:
        print("Coffee beans: Hali yetarli ✅")

    if sugar < 3:
        print("⚠️ Shakar kam qoldi!")
    else:
        print("Shakar: Hali yetarli ✅")
    print("=======================================\n")

def analytics(data):
    if not data:
        print("⚠️ Tahlil uchun mahsulot yetarli emas\n")
        return 
    
    nomlar = [m['Nomi'] for m in data]
    narxlar = [m['Narxi'] for m in data]
    soni = [m['Soni'] for m in data]

    umumiy = np.sum(narxlar)
    ortacha = np.mean(narxlar)

    print("\n============= COFFE TAHLIL ============")
    print(f"Mahsulotlarning umumiy narxi : {umumiy} so'm")
    print(f"O'rtacha narxi : {ortacha:.2f} so'm")
    print(f"Mahsulotlar ro'yxati: {nomlar}")
    print(f"Jami mahsulotlar qoldig'i (har biri): {soni}")
    print("======================================\n")

def bashorat(data):
    if len(data) < 3:
        print("⚠️ O'qitish uchun kamida 3 ta mahsulot bo'lishi kerak\n")
        return
    
    # TUZATILDI: X uchun Narxi berildi, .reshape(-1,1) mantiqiy joyga qo'yildi
    X = np.array([m['Narxi'] for m in data]).reshape(-1, 1)
    y_linea = np.array([m['Soni'] for m in data])

    chegara = 8
    y_logis = np.array([0 if m['Soni'] < chegara else 1 for m in data])

    # Train/Test split (Vergul xatosi olib tashlandi)
    X_train, X_test, y_linea_train, y_linea_test = train_test_split(X, y_linea, test_size=0.2, random_state=47)
    X_train, X_test, y_logis_train, y_logis_test = train_test_split(X, y_logis, test_size=0.2, random_state=47)

    model_lin = LinearRegression()
    model_lin.fit(X_train, y_linea_train)

    model_log = LogisticRegression()
    model_log.fit(X_train, y_logis_train)

    nomi = input("Yangi mahsulot nomi: ")
    narx = float(input("Ushbu mahsulot uchun belgilamoqchi bo'lgan narxingiz (so'm): "))

    # TUZATILDI: Bashorat qilish uchun kiruvchi qiymat massivga o'tkazilib reshape qilindi
    yangi_data = np.array([narx]).reshape(-1, 1)
    natija = model_lin.predict(yangi_data)
    holat = model_log.predict(yangi_data)

    print("\n===== AI BASHORAT NATIJASI =====")
    print(f"Agar do'konga {narx} so'mdan '{nomi}' olib kelsangiz:")
    print(f"1. [Linear AI]: Kelajakda taxminan {natija[0]:.1f} ta sotilishi kutilmoqda.")

    if holat[0] == 1:
        print("2. [Logistic AI]: 📈 Sotuv: Ko'p bo'ladi! (Kamida 8 ta yoki undan ko'p) 🎉")
    else:
        print("2. [Logistic AI]: 📉 Sotuv: Kam bo'ladi! (8 tadan kam) ❌")
    print("================================\n")

# Asosiy Menyu Sikli (Chaqirish xatolari to'liq to'g'rilandi)
while True:
    print("1. Mahsulot kiritish")
    print("2. Menyu")
    print("3. Buyurtma")
    print("4. Tarix")
    print("5. Ombor")
    print("6. Analiz")
    print("7. Bashorat")
    print("8. Chiqish")

    try:
        tanlov = int(input("Tanlang: "))
    except ValueError:
        print("Iltimos, faqat son kiriting!\n")
        continue

    if tanlov == 1:
        qosh()
    elif tanlov == 2:
        menyu(mahsulotlar)       # TUZATILDI: Argument berildi
    elif tanlov == 3:
        Buyurtma(mahsulotlar)
    elif tanlov == 4:
        tarxi(mahsulotlar)       # TUZATILDI: Argument berildi
    elif tanlov == 5:
        ombor()                  # TUZATILDI: Argument olib tashlandi
    elif tanlov == 6:
        analytics(mahsulotlar)   # TUZATILDI: Argument berildi
    elif tanlov == 7:
        bashorat(mahsulotlar)
    elif tanlov == 8:
        print("Dasturdan chiqildi! Xayr!")
        break
    else:
        print("⚠️ Bunday menyu yo'q! Qaytadan tanlang.\n")
