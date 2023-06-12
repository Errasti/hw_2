bank_account = 0
counter = 0
flag = True
while flag:
    print("1. Пополнить\n2. Снять\n3. Выйти")
    user_input = int(input())
    if user_input == 1:
        if bank_account > 5000000:
            bank_account *= 0.9
        counter += 1
        cash_in = int(input("Введите сумму пополнения кратную 50\n"))
        if counter == 3:
            bank_account += bank_account * 0.03
        bank_account += cash_in
        print("Ваш баланс = ", bank_account)
    elif user_input == 2:
        if bank_account > 5000000:
            bank_account *= 0.9
        commision = 0
        counter += 1
        if counter == 3:
            bank_account += bank_account * 0.03
        cash_out = int(input("Введите сумму снятия\n"))
        сommision = 0.015 * cash_out
        if commision < 30:
            commision = 30
        elif commision > 600:
            commision = 600
        if cash_out + commision > bank_account:
            print("Нельзя снять сумму больше чем денег на счете!")
            continue
        bank_account = bank_account - (commision + cash_out)
        print("Ваш баланс = ", bank_account)
    elif user_input == 3:
        print("Ваш баланс = ", bank_account)
        flag = False
        print("До свидания!")
