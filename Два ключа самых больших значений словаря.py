#1 СПОСОБ
my_dict = {'a':10, 'b':50, 'c':30, 'd':70, 'e':90, 'f':80}

# сначала получаем значения словаря в виде списка
values = list(my_dict.values())

# затем сортируем список по убыванию
values_sorted = sorted(values, reverse=True)

# затем получаем два самых больших значения
max_values = values_sorted[:2]

# затем находим ключи для этих значений в словаре
max_keys = [k for k, v in my_dict.items() if v in max_values]

print(max_keys) # ['e', 'f']

#2 СПОСОБ ХАРД
d = {'a': 100, 'b': 200, 'c': 300, 'd': 350}
dic = {}
dic.update(dict(sorted(d.items(), key=lambda x:x[1], reverse=True)[:2]))
print(dic)