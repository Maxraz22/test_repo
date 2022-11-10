def mane_function(y):
    if y == 1:
        return 1
    return mane_function(y-1)*y
print(mane_function(5))
print(mane_function(6))
