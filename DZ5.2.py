while True:
    first_number = input("Insert First Number : ")
    arithmetic_operator = input("Insert Arithmetic Operator (can be +, -, * or / ): ")
    second_number = input("Insert Second Number : ")

    fst = float(first_number)
    scd = float(second_number)

    if arithmetic_operator == "/" and scd == 0:
        print('Error - Cannot divide by zero')
    elif arithmetic_operator == "+":
        answer = fst + scd
    elif arithmetic_operator == "-":
        answer = fst - scd
    elif arithmetic_operator == "*":
        answer = fst * scd
    elif arithmetic_operator == "/":
        answer = fst / scd
    else: print('Input Error')

    if answer % 1 == 0:
        answer  = int(answer)

    print(first_number, arithmetic_operator, second_number, "=", answer)

    try_again = input("Type 'Yes' to try again: ")
    try_again = try_again.lower()
    if try_again == "yes":
        continue
    else:
        print("So Long")
        break
