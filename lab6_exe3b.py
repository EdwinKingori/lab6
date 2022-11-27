# The final value of x in cases where the initial value of x is 6,5 and 8.

def finalval2():
    x = 6
    while x>=5 and x<=8:
        print(x)
        if x%2 == 0:
            x = x+1
        else:
            x = x-2
        print("Final value: ", x)

finalval2()

#Value when x is 6: 7, 5, 3
#Value when x is 5: 3
#Value when x is 8: 9
