#Приклади:
#[12, 3, 4, 10] => [10, 12, 3, 4]
#[1] => [1]
#[] => []
#[12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]


lst = [1]
list_length = len(lst)
if list_length == 0:
    print(lst)
else:
    a = [lst[list_length -1]]
    b = lst[:list_length -1]
    lst = a + b
    print(lst)