import string
import keyword

prohibited_words = keyword.kwlist
prohibited_symbols = list(string.punctuation)
prohibited_symbols.remove('_')
prohibited_symbols.append(' ')

user_input = input("Insert variable name: ")

first_symbol = user_input[0]

is_valid = True

if user_input in prohibited_words:
    is_valid = False
elif "__" in user_input:
    is_valid = False
elif first_symbol.isdigit():
    is_valid = False
elif first_symbol.isupper():
    is_valid = False
else:
    for i in user_input:
        if i in prohibited_symbols:
            is_valid = False
            break
        elif i.isupper():
            is_valid = False
            break

print(is_valid)

