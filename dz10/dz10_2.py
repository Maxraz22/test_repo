import sys

def my_list(lst):
    try:
        for i in lst:
            i / 1
        mnz = set(lst)
        ind = len(lst) == len(mnz)
        ind / ind
        print("Елементи списку є унікальними.")
    except TypeError:
        print("Один з елементів не є числом.", file=sys.stderr)
    except ZeroDivisionError:
        print("У списку є однакові елементи.", file=sys.stderr)

lst1 = [1, 2, 7, 6, 8, 3, 2, 5, 5, 0]
lst2 = [1, 2, 7, 6, "t", 3, 2, 5]
lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

my_list(lst)
