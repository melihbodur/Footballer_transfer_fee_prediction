#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
a = pd.read_excel("requirement.xlsx")
from tkinter import *
from tkinter.ttk import Combobox
a.drop(["Unnamed: 0"], axis=1, inplace=True)
X = a.drop("bonservisi", axis=1)
y = a["bonservisi"]
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import scale
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import model_selection
from warnings import filterwarnings
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
filterwarnings('ignore')
gbm_tuned = GradientBoostingRegressor(learning_rate=0.01,
                                      max_depth=3,
                                      n_estimators=1000,
                                      subsample=1)

gbm_tuned = gbm_tuned.fit(X_train, y_train)
root = Tk()
root.geometry("500x600")
root.configure(background="dark slate gray")
Label(root, text="Bonservis Bedeli Tahmini", font=("Helvetica", 15, "bold"), bg="azure", relief="solid").pack()
Label(root, text="Melihbdr", relief="solid", bg="gray99").pack(side=BOTTOM)
Label(root, text="Mevkisi ", font=("Helvetica", 10, "bold"),
      bg="gray64", relief="solid", width=18).place(x=40, y=80)
Label(root, text="Ayak", font=("Helvetica", 10, "bold"),
      bg="gray64", relief="solid", width=18).place(x=40, y=130)
Label(root, text="Maaşı (Haftalık):", font=("Helvetica", 10, "bold"),
      bg="gray64", relief="solid", width=18).place(x=40, y=180)
Label(root, text="Serbest Kalma Bedeli:", font=("Helvetica", 10, "bold"),
      bg="gray64", relief="solid", width=18).place(x=40, y=230)
Label(root, text="Yaşı ", font=("Helvetica", 10, "bold"),
      bg="gray64", relief="solid", width=18).place(x=40, y=280)
Label(root, text="Oynadığı Maç Sayısı ", font=("Helvetica", 10, "bold"),
      bg="gray64", relief="solid", width=18).place(x=40, y=330)
Label(root, text="Attığı Gol Sayısı ", font=("Helvetica", 10, "bold"),
      bg="gray64", relief="solid", width=18).place(x=40, y=380)
Label(root, text="Milyon € ", font=("Helvetica", 10),
      bg="gray64").place(x=370, y=230)
Label(root, text="Milyon € ", font=("Helvetica", 15),
      bg="gray64").place(x=250, y=500)
def mevki():

    bölge = mevki_kutu.get()
    if (bölge == "Ofansif Orta Saha"):
        mevkisi = 0
    elif (bölge == "Stoper"):
        mevkisi = 1
    elif (bölge == "Defansif Orta Saha"):
        mevkisi = 2
    elif (bölge == "Gizli Forvet"):
        mevkisi = 3
    elif (bölge == "Orta Saha"):
        mevkisi = 4
    elif (bölge == "Kaleci"):
        mevkisi = 5
    elif (bölge == "Sol Bek"):
        mevkisi = 630
    elif (bölge == "Sol Kanat"):
        mevkisi = 7
    elif (bölge == "Sağ Bek"):
        mevkisi = 8
    elif (bölge == "Sağ Kanat"):
        mevkisi = 9
    elif (bölge == "Forvet"):
        mevkisi = 10
    return mevkisi
def ayak():
    global ayağı
    ayak = ayak_kutu.get()
    if (ayak == "Sağ Ayak"):
        ayağı = 1
    elif (ayak == "Sol Ayak"):
        ayağı = 0

    return ayak
maş = StringVar()
srbst = StringVar()
yaş = StringVar()
ttlmaç = StringVar()
attıgol = StringVar()

mevkisi = Entry(root)
ayağı = Entry(root)
mevkiler = ["Ofansif Orta Saha", "Stoper", "Defansif Orta Saha","Gizli Forvet", "Orta Saha", "Kaleci", "Sol Bek",
            "Sol Kanat", "Sağ Bek", "Sağ Kanat", "Forvet"]

mevki_kutu = Combobox(root, values=mevkiler)
mevki_kutu.place(x=210, y=80)
ayakk = ["Sağ Ayak", "Sol Ayak"]
ayak_kutu = Combobox(root, values=ayakk)
ayak_kutu.place(x=210, y=130)
Button(root, text="Seç", command=mevki).place(x=370, y=80)
Button(root, text="Seç", command=ayak).place(x=370, y=130)
Entry(root, text=maş, width=25).place(x=210, y=180)
Entry(root, text=srbst, width=25).place(x=210, y=230)
Entry(root, text=yaş, width=25).place(x=210, y=280)
Entry(root, text=ttlmaç, width=25).place(x=210, y=330)
Entry(root, text=attıgol, width=25).place(x=210, y=380)
def info():
    n = Tk()
    n.geometry("600x120")
    n.configure(background="gray80")
    Label(n, text="Linkdn = https://www.linkedin.com/in/melihbdr/ ", font=("Helvetica", 10, "bold"),
          bg="gray80", relief="solid").place(x=40, y=40)
    Label(n, text="Youtube = https://www.youtube.com/channel/UCtvccweD3LKUPrCfW9w3wvg ", font=("Helvetica", 10, "bold"),
          bg="gray80", relief="solid").place(x=40, y=70)

    n.resizable(0, 0)
    n.mainloop()
Button(root, text="İletişim", width=15, height=2, command=info).place(x=70, y=550)
def model():
    X_test = [(mevkisi), (ayağı), float(maş.get()), float(srbst.get()), int(yaş.get()), int(ttlmaç.get()),
              int(attıgol.get())]

    y_pred = gbm_tuned.predict([X_test,])

    Label(root, text=round(y_pred[0], 2), font=("Helvetica"), bg="gray80", relief="solid", width=15).place(x=70, y=500)
Button(root, text="Tahmini Bonservis Bedeli :", width=25, command=model).place(x=70, y=450)
Button(root, text="kapat", width=15, command=root.destroy).place(x=0, y=0)
root.resizable(0, 0)
root.mainloop()

