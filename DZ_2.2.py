user_input = int(input("Enter 5-Digit Number: "))
first_number = user_input // 10000
second_number = user_input // 1000 % 10
third_number = user_input // 100 % 10
fourth_number = user_input // 10 % 10
fifth_number = user_input %10

output = (fifth_number*10000 + fourth_number*1000 + third_number*100 + second_number*10 + first_number*1)
print("Inserted number in reverse order: ",output)
