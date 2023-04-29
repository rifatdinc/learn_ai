
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('eksikveriler.csv')

boy = veriler[['boy']]

print(boy) 

boykilo = veriler[['boy','kilo']]

print(boykilo)

x=10

class insan:
    boy= 180
    def run(self,b):
        return b+10
    
rafi = insan()
print(rafi.boy)
print(rafi.run(90))


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

Yas = veriler.iloc[:,1:4].values

print(Yas)

imputer = imputer.fit(Yas[:,1:4])

Yas[:,1:4] = imputer.transform(Yas[:,1:4])

print(Yas)

ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

print(list(range(22)))

sonuc = pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','us'])

print(sonuc)
# how to git config 
# git config --global user.name "Rifat Dinc"
# git config --global user.email "rafidinc41@gmail.com"