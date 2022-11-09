def mane_function(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return mane_function(n-1)+mane_function(n-2)
print(mane_function(7))
print(mane_function(8))
print(mane_function(9))