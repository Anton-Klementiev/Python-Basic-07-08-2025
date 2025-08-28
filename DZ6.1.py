import string
letters = list(string.ascii_letters)

user_input = list(input("Insert two letters with hyphen between them: "))

first_letter, second_letter = user_input[0], user_input[2]
output_list = letters[letters.index(first_letter):letters.index(second_letter)+1]
output_string = "".join(output_list)
print(output_string)
