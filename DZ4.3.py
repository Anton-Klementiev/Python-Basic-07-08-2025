#[1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
#[1, 1, 2, 1] == [1, 2, 2]
#[6, 3, 7] == [6, 7, 3]

import random

lst = [random.randint(0,9) for i in range(random.randint(3, 10))]
new_list = [lst[0],lst[2],lst[-2]]

print("Generated list:", lst)
print("New List:", new_list)
