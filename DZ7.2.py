text = input("Please enter a text: ")
def correct_sentence(text):
    a = text[0]
    b = text[-1]
    if not a.isupper():
        text = a.upper() + text[1:]
    if b != ".":
        text += "."
    return text

#assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
#assert correct_sentence("hello") == "Hello.", 'Test2'
#assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
#assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
#assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')