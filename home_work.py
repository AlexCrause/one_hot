"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import pandas as pd
import random

lst = ['robot'] * 10  # Создаем список из 10 элементов 'robot'
lst += ['human'] * 10  # Добавляем к списку 10 элементов 'human'
random.shuffle(lst)  # Перемешиваем элементы списка
data = pd.DataFrame({'whoAmI': lst})  # Создаем DataFrame с одним столбцом 'whoAmI'

data['robot'] = (data['whoAmI'] == 'robot').astype(int)  # Создаем столбец 'robot'
data['human'] = (data['whoAmI'] == 'human').astype(int)  # Создаем столбец 'human'

print(data.head(11))
