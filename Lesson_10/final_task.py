'''Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Надо это сделать без get_dummieНs.'''

import pandas as pd
from random import shuffle

lst = ['robot'] * 10
lst += ['human'] * 10

shuffle(lst)

robot_lst = (1 if el == 'robot' else 0 for el in lst)
human_lst = (1 if el == 'human' else 0 for el in lst)

data = pd.DataFrame({'human': human_lst, 'robot': robot_lst})

print(data.head(20))


