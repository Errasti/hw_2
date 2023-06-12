number = int(input("Введите десятичное число: "))
result = ''
alphabet = '0123456789ABCDEF'
print(hex(number))
while number > 0:
    result = alphabet[number % 16] + result
    number = number // 16
print("Ответ - ", result)
