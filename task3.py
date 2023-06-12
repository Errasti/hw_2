fract_one = input("Введите первую дробь\n").split("/")
fract_two = input("Введите вторую дробь\n").split("/")
mutual_denom = int(fract_one[1]) * int(fract_two[1])
numerator_one = int(fract_one[0]) * int(fract_two[1])
numerator_two = int(fract_two[0]) * int(fract_one[1])
div_sum = (numerator_one + numerator_two) / mutual_denom
div_mult = (int(fract_one[0]) * int(fract_two[0])) / (int(fract_one[1]) * int(fract_two[1]))

print("Сумма дробей - ", div_sum, "Произведение дробей - ", div_mult)
