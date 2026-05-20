import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

data = {
    'masofa': [1, 2, 3, 4, 5],
    'narx': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)
x = df['masofa'].values.reshape(1,-1)
y = df['narx'].values
# 2. Bo'sh model yaratamiz
ai_model = LinearRegression()

# 3. Modelni o'qitamiz (fit funksiyasi - o'rganish buyrug'i)
ai_model.fit(x, y)
print("Ajoyib! Sun'iy intellekt ma'lumotlarni o'rgandi va qoidani topdi.")
# 4. Yangi masofalarni beramiz (ustun ko'rinishida)
yangi_mijoz = pd.DataFrame({'Masofa': [30, 50]})

# 5. Bashorat qilish (predict funksiyasi)
javoblar = ai_model.predict(yangi_mijoz)

print("\n--- AI BASHORATI ---")
print(f"30 km uchun narx: {int(javoblar[0])} so'm")
print(f"50 km uchun narx: {int(javoblar[1])} so'm")
