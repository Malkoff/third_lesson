element = int (input ('Введите количество элементов: '))
numbers = []
for i in range (element):
    number = int (input ('Введите число: '))
    numbers.append(number)
numbers.sort()
print(numbers)