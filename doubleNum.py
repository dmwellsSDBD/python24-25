'''
Input a series of numbers and see what their power of 2 is.
'''
def pow2(y):
    powOf2 = y ** 2
    # return powOf2
    print(y, "to the 2nd power is: ", powOf2)

myNumbers = [2, 5, 12, 17, 25, 32]

for i in myNumbers:
    pow2(i)

# pow2(17)
    
print("Our function is complete.")