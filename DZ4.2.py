#[0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

#[1, 3, 5] => 30
#[6] => 36
#[] => 0

lst = [0, 1, 7, 2, 4, 8]

if len(lst) == 0:
    result = 0
else:
    last_element = lst[-1]
    even_index = lst[::2]
    result = sum(even_index) * last_element

print("Result:",result)