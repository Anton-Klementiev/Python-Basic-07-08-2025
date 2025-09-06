lst = [1, 2, 3, 4]

def add_one(lst):
    lst2 = []
    for x in lst:
        lst2.append(str(x))
    num = str(int("".join(lst2))+ 1)
    #create a new list by splitting values of this int into list
    new_lst = []
    for i in num:
        new_lst.append(int(i))
    #return this shit
    return new_lst
print(add_one(lst))

#assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
#assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
#assert add_one([0]) == [1], 'Test3'
#assert add_one([9]) == [1, 0], 'Test4'
print("ОК")