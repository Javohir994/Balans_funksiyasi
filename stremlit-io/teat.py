import streamlit as st
import os 

st.set_page_config(page_title='BMW UZB', layout='wide')

st.markdown("""
    <style>
    /* 1. Umumiy sayt foni (O'rtacha och kulrang) */
    .stApp {
        background-color: #f0f2f5 !important;
    }
    
    /* 2. Barcha matnlarni to'q qora qilish (Ko'rinishi uchun) */
    h1, h2, h3, h4, h5, h6, p, label, span, li {
        color: #1a1a1a !important;
    }
    
    /* 3. Tab tugmalarini to'q rang va qalin qilish */
    .stTabs [data-baseweb="tab"] {
        font-size: 20px;
        font-weight: bold;
        padding: 10px 40px;
        color: #2b2b2b !important;
    }
    
    /* 4. Input (Ism, telefon yozadigan joylar) fonini oq va atrofini qora chiziqli qilish */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 1px solid #999999 !important;
        border-radius: 8px !important;
    }
    
    /* Input ichidagi yozilayotgan matn rangi */
    input {
        color: #000000 !important;
    }
    
    /* 5. Jadval (Table) ichidagi matnlar to'liq qora va aniq ko'rinishi uchun */
    .stTable td, .stTable th {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stTabs [data-baseweb="tab"] {
        font-size: 20px;
        font-weight: bold;
        padding: 10px 40px;
    }
    </style>
""", unsafe_allow_html=True)

if 'bmw' not in st.session_state:
    st.session_state.bmw =[]

st.title("BMW UZB MOTORS")

tab1, tab2, tab3, tab4 = st.tabs(["Yangiliklar",  "BMW Haqida",  "BMW Oylik to'lov",   "BMW M modellar"  ])

with tab1:
    st.subheader("Yangiliklar bo'limi")
    
    download =  "/home/javohir/Downloads"
    rasm = os.path.join(download, '2027 BMW X5 (G65)_ Neue Klasse-SUV mit Elektro, Hybrid, Diesel, Benziner und Wasserstoff.jpeg')

    if os.path.exists(rasm):
        st.image(rasm)

    st.markdown(
        '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">BMW X5</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
    '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">394 hp</h1>', 
    unsafe_allow_html=True
)
    st.markdown(
    '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Horsepower</p>', 
    unsafe_allow_html=True
)

    st.markdown(
    '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">155 mph</h1>',
    unsafe_allow_html=True
)

    st.markdown(
    '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Top speed</p>',
    unsafe_allow_html=True
)


    st.subheader("Yangi BMW X5 yo‘ltanlamasi — sizga qanday qulay bo‘lsa, shunday.")

    st.info("BMW X5 oldinda, boshqalari esa undan keyin keladi.  " \
    "Haydash tizimi uchta ilg'or motor variantlarini o'z ichiga olgan holda haqiqiy tanlov erkinligini ta'minlaydi." \
    " Aqlli AI qo'llab-quvvatlashi bilan yordam tizimlari sizni nazorat ostida qoldiribuyg'un ishlaydi, bu esa ko'proq xavfsizlik, qulaylik va haydash zavqini oshiradi. Qisqa va uzoq sayohatlar, hatto gavjum yo'llarda ham yanada taskin beradi.")

with tab2:
    st.subheader("Uzoq yillik sadoqat.")
    st.write("Innovatsiyalarga qaratilgan tinimsiz e’tiborimiz yangilik emas." \
    " Aslida, ilk elektromobilimiz yo‘lga chiqqaniga 50 yildan oshdi.")

    download =  "/home/javohir/Downloads"
    rasm = os.path.join(download, 'The Coolest Cars of the 1970s.jpeg')
    if os.path.exists(rasm):
        st.image(rasm)

    st.subheader("BMW 1972")
    st.info("Myunxendagi Olimpiya o'yinlarida" \
    " namoyish etilgan ushbu jo'shqin sport" \
    " avtomobili birinchi elektr BMWga aylanadi.")


    st.subheader("BMW 2000")
    st.info("Barqarorlik rasman BMW korporativ" \
    " strategiyasining asosiy tamoyiliga aylanadi.")

with tab3:
    st.subheader("BMW sizga katta imkoniyatlar eshigini ochadi.")
    st.write("BMW oilasi safida qoling va ajoyib taklifdan foydalaning. 2-avgustga qadar yangi "
             "BMW avtomobilini lizingga olish yoki"\
              " xarid qilishda maxsus Sodiqlik krediti (Loyalty Credit) imkoniyatiga ega bo‘ling.")
    
    st.subheader("Mos modellar va mavjud takliflar $ da")
    st.info("2 Series Gran Coupe (228i, M235i xDrive):  $1,000 (2026)")

    st.info("3 Series (330i, M340i): $2,000 (2025), $1,000 (2026)")

    st.info("5 Series (530i, 540i xDrive): $2,000 (2025), $2,000 (2026)")

    st.info("8 Series (All models): $2,500 (2025), $2,500 (2026)")

    st.link_button("💬 BMW bilan bog'lanish uchun Telegram yozing", "https://t.me")

with tab4:
    st.subheader("BMW M modellar")

    bmw_m = st.radio("BMW M modellini tanlang:", 
        ["BMW M2 Coupe", "BMW M3 Competition", "BMW M4 Competition", "BMW M5 Competition"])

    if bmw_m == "BMW M2 Coupe":
        download =  "/home/javohir/Downloads"
        rasm = os.path.join(download, 'BMW M2 50 Years Special Edition Coupe.jpeg')
        if os.path.exists(rasm):
            st.image(rasm)

            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;"> BMW M2 Coupe</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">4.1 sec</h1>',
                unsafe_allow_html=True
                )
            
            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">0-60 mph</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">473 hp</h1>',
              
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Horsepower</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">$69,000</h1>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Starting Price</p>',
                unsafe_allow_html=True
            )

    elif bmw_m == "BMW M3 Competition":
        download = "/home/javohir/Downloads"
        ras = os.path.join(download, 'G80 M3 - Nitron NTR R1 Coilovers & BBS RT88.jpeg')
        if os.path.exists(ras):
            st.image(ras)

            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;"> BMW M3 Competition</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">3.4 sec</h1>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">0-60 mph</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">503 hp</h1>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Horsepower</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">$70,895</h1>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Starting Price</p>',
                unsafe_allow_html=True
            )      
    
    elif bmw_m == "BMW M4 Competition":
        download = "/home/javohir/Downloads"
        ra = os.path.join(download, 'Isle of Man Green G82 M4 - Autotecknic, Aurora, Suvneer.jpeg')
        if os.path.exists(ra):
            st.image(ra)

            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;"> BMW M4 Competition</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">3.4 sec</h1>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">0-60 mph</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">503 hp</h1>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Horsepower</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">$72,795</h1>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Starting Price</p>',
                unsafe_allow_html=True
            )

    elif bmw_m == "BMW M5 Competition":

        download = "/home/javohir/Downloads"
        r = os.path.join(download, '_.jpeg')
        if os.path.exists(r):
            st.image(r)

            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;"> BMW M5 Competition</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">3.1 sec</h1>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">0-60 mph</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">617 hp</h1>',
                unsafe_allow_html=True
            )
            
            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Horsepower</p>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<h1 style="text-align: center; font-size: 55px; margin-bottom: 0px;">$104,995</h1>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<p style="text-align: center; font-size: 20px; color: gray; margin-top: 0px;">Starting Price</p>',
                unsafe_allow_html=True
            )