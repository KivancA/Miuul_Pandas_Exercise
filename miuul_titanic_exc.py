# -*- coding: utf-8 -*-
"""miuul_titanic_exc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Rn2jT9MHZnTVL7GordIg_HdA1OmSdyQ

⛵**TITANIC** ***MIUUL PANDAS EXERCISE***
"""

import pandas as pd
import seaborn as sns
###Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df = sns.load_dataset("titanic")

###Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
sex=df["sex"].value_counts()
print(sex)

###Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
unique_counts = df.nunique()
print(unique_counts)

###Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz
unique_pclass_values = df["pclass"].nunique()
print("pclass değişkenine ait unique değerlerinin sayısı:", unique_pclass_values)

###Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
unique_pclass = df['pclass'].nunique()
unique_parch = df['parch'].nunique()

print("pclass unique değer sayısı:", unique_pclass)
print("parch unique değer sayısı:", unique_parch)

###Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
print("embarked değişkeninin veri tipi:", df["embarked"].dtypes)
df["embarked"] = df["embarked"].astype("category")
print("embarked değişkeninin güncellendikten sonraki veri tipi:", df["embarked"].dtypes)

###Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
embarked_cpassengers = df[df["embarked"] == "C"]
print(embarked_cpassengers)

###Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
embarked_nonspassengers = df[df["embarked"] != "S"]
print(embarked_nonspassengers)

###Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
youngfem = df[(df["age"] < 30) & (df["sex"] == "female")]
print(youngfem)

###Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
newfare = df[(df['fare'] > 500) | (df['age'] > 70)]
print(newfare)

###Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
missval = df.isnull().sum()
print(missval)

###Görev 12: who değişkenini dataframe’den çıkarınız.
df.drop('who', axis=1, inplace=True)
print(df)

###Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
deck_mode = df['deck'].mode().iloc[0]
df['deck'].fillna(deck_mode, inplace=True)
print(df)

###Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
age_medyan = df['age'].median()
df['age'].fillna(age_medyan, inplace=True)
print(df)

###Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
onbes = df.groupby(['pclass', 'sex'])['survived'].agg(['sum', 'count', 'mean'])
print(onbes)

###Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
## setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
def age_flag(row):
    if row['age'] < 30:
        return 1
    else:
        return 0
df['age_flag'] = df.apply(lambda row: age_flag(row), axis=1)
print(df)

###Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
tips = sns.load_dataset('tips')
print(tips.head())

###Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
onsekiz = tips.groupby('time')['total_bill'].agg(['sum', 'min', 'max', 'mean'])
print(onsekiz)

###Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
ondokuz = tips.groupby(['day', 'time'])['total_bill'].agg(['sum', 'min', 'max', 'mean'])
print(ondokuz)

###Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
yirmi = tips[(tips['time'] == 'Lunch') & (tips['sex'] == 'Female')].groupby('day')[['total_bill', 'tip']].agg(['sum', 'min', 'max', 'mean'])
print(yirmi)

###Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
fil = tips.loc[(tips['size'] < 3) & (tips['total_bill'] > 10)]
ort= fil['total_bill'].mean()
print("Ort total_bill değeri:", ort)

###Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
tips['total_bill_tip_sum'] = tips['total_bill'] + tips['tip']
print(tips)

###Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
tips['total_bill_tip_sum'] = tips['total_bill'] + tips['tip']
newtips = tips.sort_values(by='total_bill_tip_sum', ascending=False)
otuz = newtips.head(30)
print(otuz)