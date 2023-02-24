str_number = input ('Введите числа: ')
numbers = str_number.split(',')
results = []
for number in numbers:
    if numbers.count(number) == 1:
        results.append(number)

print(results)