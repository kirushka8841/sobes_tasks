# Необходимо написать функцию, которая проверит строку на то, является ли она палиндромом
# Доп условия:
# 1. Из строки нужно удалить все не буквенно циферные значения
# 2. Привести все символы строки к верхнему\нижнему регистру

s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'

# Функция isalnum() возвращает значение True, если строка является буквенно-цифровой. 
def isPalindrom(s: str) -> bool:
    palindrom = [symbol for symbol in s.lower() if symbol.isalnum()]
    return palindrom == palindrom[::-1]

print(isPalindrom(s1))
print(isPalindrom(s2))