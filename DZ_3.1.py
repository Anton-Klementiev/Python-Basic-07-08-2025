#to check if it's only supposed to be an integer - change to float if it isn't
first_number = int(input("Insert First Number : "))
second_number = int(input("Insert Second Number : "))
arithmetic_operator = input("Insert Arithmetic Operator (can be +, -, * or / ): ")

if arithmetic_operator == "/" and second_number == 0:
    print('Error; Cannot divide by zero')
elif arithmetic_operator == "+":
    answer = first_number + second_number
    print(first_number, arithmetic_operator, second_number, "=", answer)
elif arithmetic_operator == "-":
    answer = first_number - second_number
    print(first_number, arithmetic_operator, second_number, "=", answer)
elif arithmetic_operator == "*":
    answer = first_number * second_number
    print(first_number, arithmetic_operator, second_number, "=", answer)
elif arithmetic_operator == "/":
    answer = first_number / second_number
    print(first_number, arithmetic_operator, second_number, "=", answer)
else: print('Input Error')

