#[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
#[1, 2, 3] => [[1, 2], [3]]
#[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
#[1] => [[1], []]
#[] => [[], []]

lst = []
if len(lst) % 2 == 0:
    first_list = lst[0:len(lst)//2]
    second_list = lst[len(lst)//2:]

elif len(lst) % 2 != 0:
    first_list = lst[0:(len(lst)//2)+1]
    second_list = lst[(len(lst)//2)+1:]

result = [first_list] + [second_list]
print(result)