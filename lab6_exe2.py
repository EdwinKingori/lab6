# dividing a number by 2 using a while loop.

def main():

# using x>0 or X!=0 generates simiar results to x> 0.0

    x = 1.0
    count = 0
    
    while x > 0:
        print(f"The result of x divided by 2 is:")
        x = x/2
        count += 1 # finds how many steps x reaches the vaue 0
        print (x)
    print(f"x reaches the value of 0 in {count} times ")

main()
