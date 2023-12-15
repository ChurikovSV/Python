'''Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}'''

def print_value(dict):
    my_list = []
    for i in dict:
        for key, value in i.items():
            my_list.append(value.strip())
    
    return set(my_list)



dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
{" VIII":" S007 "}]

print(print_value(dict_list))