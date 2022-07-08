import random
import string

set = random.randint(1, 11)
if set % 2 == 0:
    symbol = random.choice(string.ascii_letters)
else:
    symbol = random.choice(string.punctuation)

symbol2 = random.choice(string.punctuation)
table = {x:random.choice(string.ascii_letters) for x in range(1,100)}

for key in table:
    if key % 2 == 0 or key // 2 == 1:
        while True:
            choice = random.choice(string.punctuation)
            if choice == symbol:
                continue
            else:
                table[key]=choice
                break

for key in table:
    if key % 9 == 0 or key / 9 == 1:
        table[key]=symbol
    if key % 7 == 0 and key % 9 != 0 and key / 9 != 1:
        table[key]=symbol2

if set % 2 == 0:
    for key in range(set, 99, 34):
        table[key]=symbol
else:
    for key in range(set, 88, 43):
        table[key]=symbol

print('==================Угадыватель мыслей 3000=======================','\n')
print('1. Загадайте любое положительное двузначное число')
print('2. Вычтите из него составляющие его цифры (например, 55 - 5 - 5 = 45)')
print('3. ЗАПОМНИТЕ полученное число')
input('Нажмите Enter для продолжения...')
print('4. Найдите это число в таблице и символ, которому оно соответствует')
print('5. Подумайте об этом символе и нажмите Enter, как будете готовы. Программа отобразит этот символ')
print('\n',str(table).replace('{','').replace('}',''),'\n')
input('Нажмите Enter для продолжения...')
print(f'Ваш символ: {symbol}')
