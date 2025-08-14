user_input = int(input("Enter 5-Digit Number: "))
first_number = user_input // 10000
second_number = user_input // 1000 % 10
third_number = user_input // 100 % 10
fourth_number = user_input // 10 % 10
fifth_number = user_input %10
print("Inserted number in reverse order: ",fifth_number,fourth_number,third_number,second_number,first_number)
