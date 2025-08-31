result = input("Enter a number: ")

while int(result) > 9:
    n = 1
    for i in result:
        n *= int(i)
    result = str(n)

print(result)