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