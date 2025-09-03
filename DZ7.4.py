#Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів, за наступними правилом:
#Один список з числами кратними 3, інший з кратними числами 5.
#За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
#Функція повинна повернути цю множину як результат своєї роботи.

def common_elements():
    lst1 = list(range(0,100,3))
    lst2 = list(range(0,100,5))
    set1 = set(lst1)
    set2 = set(lst2)

    iters_set = set1.intersection(set2)
    return iters_set

print(common_elements())
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}