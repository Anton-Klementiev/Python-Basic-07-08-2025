
text = input("Insert text: ")
some_str = input("Insert search key: ")

def second_index(text, some_str):
    frst = text.find(some_str)
    scnd = text.find(some_str, frst + 1)
    if scnd == -1:
        return None
    else: return second_index

#assert second_index("sims", "s") == 3, 'Test1'
#assert second_index("find the river", "e") == 12, 'Test2'
#assert second_index("hi", "h") is None, 'Test3'
#assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')