# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

#data = np.genfromtxt('gbp.csv', encoding="unicode_escape",delimiter='","',names=True)
data = pd.read_csv('gbp.csv', sep='","')
for i, col in enumerate(data.columns):  # Замена лишних " на пустоту
    data.iloc[:, i] = data.iloc[:, i].str.replace('"', '')
data = data.apply(pd.to_numeric, errors='coerce')  # перевод строк в числовые
a = np.ones(data.shape)
res = data*a
print(data)
print(a)
print(res)