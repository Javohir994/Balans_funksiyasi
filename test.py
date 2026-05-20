import pandas as pd
import numpy as np
#Dastur nomi
print("=====SCHOOL MANAGEMENT SYSTEM=====")
#bosh list
oquvchilar = []
#malumot 1
df1 = pd.DataFrame({
    "Ism_1":["Ali"],
    "Sinf_1":["1A"]
})
#malumot 2
df2 = pd.DataFrame({
    "Ism_2":["Vali"],
    "Sinf_2":["1G"]
})
#merge
df = pd.merge(df1, df2, left_on="Ism_1", right_on="Ism_2", how="outer")
#groupby
d1 = df.groupby("Sinf_2")["Sinf_1"].mean()
print(d1)
#fillna
d = df.fillna({
    "Ism_1":"Gani",
    "Sinf_1":"1B",
    "Ism_2":"Soli",
    "Sinf_2":"1V"
})
#tuple
tup = ("Avvalgi o'quvchilar",)
print(tup)
#concat va axis
dw = pd.concat([df1,df2,],axis=1)
print(dw)
#set
se = {"Hozirgi o'quvchilar"}
print(se)
print(d)
#def qoshish
def qosh():
    ism = input("Student ismi:")
    yosh = int(input("Yoshi:"))
    sinf = input("Sinf:")
    oquvchi = {"Ism":ism, "Yosh":yosh, "Sinf":sinf}
    oquvchilar.append(oquvchi)
    print("✅ Student qo'shildi")
#techer qoshish
def teach():
    teac = input("Teacher:")
    fan = input("Fan:")
    oqituvchi = {"Teacher":teac, "Fan":fan}
    oquvchilar.append(oqituvchi)
    print("✅ Teacher qo‘shildi")
#davomat
def dova():
    ism = input("Ismi :")
    holat = input("Holati :")
    davomat = {"Ismi":ism, "Holat":holat}
    oquvchilar.append(davomat)
    print("✅ Davomat saqlandi")
#exam
def exam():
    ism = input("Ismi :")
    fan1 = int(input("Matematika :"))
    fan2 = int(input("English :"))
    fan3 = int(input("Fizika :"))
    exzamin = {"Ism":ism, "Matematika":fan1, "English":fan2, "Fizika":fan3}
    oquvchilar.append(exzamin)  
    print("✅ Natija saqlandi")
#korish funksiyasi
def korish(data):
    if not data:
        print("Savat bosh!")
        return
    for oquv in oquvchilar:
        print({"Ism":[oquv], "Yosh":[oquv], "Sinf":[oquv]})
#ranking funksiyasi
def rank(df):
    if "Ball" not in df.columns:
        print("❌ Ball yo‘q")
        return
    sorted_df = df.sort_values(by="Ball", ascending=False)
    print("===== RANKING =====")
    for i, row in enumerate(sorted_df.itertuples(), start=1):
        print(i, row.Ism, row.Ball)
#statis
def statis(data):
    if not data:
        print("Savat bo'sh!")
        return
    all_score = df[["Matematika", "English", "Fizika" ]]
    print("=============================")
    print("O'rtacha:", np.mean(all_score))
    print("Eng ko'p:", np.max(all_score))
    print("Eng kam:", np.min(all_score))
    print("=============================")
#csvga saqlash
def csv(data):
    if not data:
        print("Savat bo'sh!")
        return
    dg = pd.DataFrame(data)
    dg.to_csv("talaba.csv", index=False)
#loop
while True:
    print("======================")
#qoidasi
    print("1 qo'shish")
    print("2 teacher qo'shish")
    print("3 Davomat qo'shish")
    print("4 examin natija qo'shish")
    print("5 studentlarni ko'rish")
    print("6 Ranking")
    print("7 statistika")
    print("8 csvga saqlash")
    print("9 chiqish")
    print("======================")
#tanlash
    tanlov = int(input("Tanlang :"))
#if elif else funksiya
    if tanlov == 1:
        qosh()
    elif tanlov == 2:
        teach()
    elif tanlov == 3:
        dova()
    elif tanlov == 4:
        exam()
    elif tanlov == 5:
        korish(oquvchilar)
    elif tanlov == 6:
        rank(oquvchilar)
    elif tanlov == 7:
        statis(oquvchilar)
    elif tanlov == 8:
            csv()
    elif tanlov == 9:
        print("xayr!")
        break
    else:
        print("Xato!")