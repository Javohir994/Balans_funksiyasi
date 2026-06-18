import streamlit as st
import numpy as np

st.title("🚗 Avtosalon Analitika Tizimi")

# 1. Xotirani to'g'ri tekshirish va yaratish
if 'moshina' not in st.session_state:
    st.session_state.moshina = []  # To'g'ri nomlandi

with st.sidebar:
    # Nomlarni tekshirish uchun aniq qilib yozib oldik
    tanlov = st.radio("Tanlovni tanlang:", [
        'Moshina qoshish',  
        'Moshina narxlarni korish', 
        'Moshina narxni somga aylantirish', 
        'Ochirish'
    ])

if tanlov == 'Moshina qoshish':
    st.subheader("Yangi moshina qoshish")
    
    nomi = st.text_input("Mo'shina nomi : ")
    yil = st.number_input("Yili :", min_value=0, step=1)
    probeg = st.number_input("Probeg :")
    narx = st.number_input("Narxi (dollarda $ ) :", min_value=0, step=1)
    
    # Formasiz ishlashi uchun oddiy st.button qildik
    submit = st.button("Kiritish")
    if submit:
        if nomi and narx > 0:
            yangi = {'Nomi': nomi, 'Yil': yil, 'Probeg': probeg, 'Narxi': narx}
            st.session_state.moshina.append(yangi)
            st.success(f"{nomi} muvaffaqiyatli qo'shildi!")
        else:
            st.warning("Iltimos, moshina nomi va narxini kiriting!")

elif tanlov == 'Moshina narxlarni korish': # Nom radiodagi bilan bir xil qilindi
    st.subheader("Moshinalar ro'yxati")
    if not st.session_state.moshina:
        st.warning("Savat bo'sh")
    else:
        st.table(st.session_state.moshina)

        # NumPy uchun faqat narxlarni ajratib olamiz (Loop yordamida)
        narxlar_listi = [m['Narxi'] for m in st.session_state.moshina]
        moshina_arr = np.array(narxlar_listi) # Endi ichida faqat sonlar bor

        st.info(f"💎 Eng qimmat moshina: {np.max(moshina_arr):,.0f} $")
        st.success(f"📈 Ortacha moshina narxi: {np.mean(moshina_arr):.2f} $")
        
        st.markdown("---")
        # TOPshiriqdagi SET va LOOP qismi (Modellarni sanash)
        st.subheader("📋 Salondagi modellar soni:")
        modellarni_ajratish = [m['Nomi'] for m in st.session_state.moshina]
        unikal_modellar = set(modellarni_ajratish) # SET orqali takrorlanmas qildik
        
        for model in unikal_modellar:
            sanoq = modellarni_ajratish.count(model) # LOOP ichida sanash
            st.write(f"- **{model}** modelidan: {sanoq} ta bor.")

elif tanlov == 'Moshina narxni somga aylantirish': # Nom to'g'rilandi
    st.subheader("Dollar | uzs")

    def somga_ogirish(dollar):
        kurs = 13000  # Kurs 13000 so'm qilindi
        jami = kurs * dollar
        return jami

    ism = st.text_input("Ismingizni kiriting")
    summa = st.number_input("Kerakli summani kiriting (dollarda $) :", min_value=0)

    if st.button("Bo'sish", type='primary'):
        if ism and summa > 0:
            savat = somga_ogirish(summa)
            st.info(f"Muhtaram {ism} : {summa:,.0f} $ miqdori: {savat:,.2f} so'm bo'ladi")

            st.markdown("### 📄 Xarid Cheki")
            st.code(f"""
===========================
Mijoz: {ism}
Kiritilgan summa: {summa:,.0f} $
Kurs: 1 $ = 13,000 so'm
---------------------------
JAMI TO'LOV: {savat:,.2f} so'm
===========================
            """)
        else:
            st.warning("Iltimos hammasini to'ldiring")
    
elif tanlov == 'Ochirish':
    st.warning("Diqqat! Bu harakat oxirgi ma'lumotni o'chirib tashlaydi!")
    if not st.session_state.moshina:
        st.info("O'chirish uchun moshina yo'q, ro'yxat bo'sh.")
    else:
        if st.button("Oxirgisini ochirish", type="primary"):
            st.session_state.moshina.pop() # Oxirgisini o'chirish
            st.success("Muvaffaqiyatli ochirildi!")
            st.rerun()
