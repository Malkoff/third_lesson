elements = int (input ('Введите элементы 1 списка: '))
numbers = []
for i in range (elements):
    number = int (input ('Введите число: '))
    numbers.append(number)

sec_elements = int (input ('Введите элементы 2 списка: '))
sec_numbers = []
for i in range (sec_elements):
    sec_number = int (input ('Введите число: '))
    sec_numbers.append(sec_number)

for results in numbers.copy():
    if results in sec_numbers:
        numbers.remove(results)

print(numbers)