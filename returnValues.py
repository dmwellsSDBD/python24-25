def sum(first, second):
    total = first + second
    return total

def add_one(x):
    return x + 1 # This X variable

result = sum(5, 8)
print(result) # 13

x = sum(10, 20) # BUT WAIT - Don't we already have a variable called x? Different from this X variable
print(x) # 30

y = add_one(100)
print(y) # 101

z = add_one(y)
print(z) # 102