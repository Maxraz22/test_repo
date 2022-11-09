def mane_function(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return mane_function(n-1)+mane_function(n-2)
print(mane_function(7))

def test_function(x):
    if x<5:
        print(x)
        test_function(x+1)
test_function(1)
test_function(2)
test_function(3)

