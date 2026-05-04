import psycopg2

# 1. Bazaga ulanish
conn = psycopg2.connect(
    dbname="bazangiz_nomi", 
    user="postgres", 
    password="parolingiz", 
    host="localhost"
)
cursor = conn.cursor()

# 2. SQL buyrug'ini matn (string) ko'rinishida yozish
# E'tibor bering: Python'da matn ichida (') belgisi bo'lsa, 
# tashqaridan uchta qo'shtirnoq """ ishlatish xavfsizroq.
sql_query = """
INSERT INTO kitoblar (nomi, muallif, narxi, mavjudmi)
VALUES ('O''tkan kunlar', 'Abdulla Qodiriy', 45000, true);
"""

# 3. Buyruqni bajarish
cursor.execute(sql_query)
conn.commit()

# 4. Ulanishni yopish
cursor.close()
conn.close()
