#1a
def main():
    sum = 0
    for i in range (100 +1):
        sum = sum + i;
    print(sum)
main()
# using th while loop to acheiev the same result
def using_while ():
    sum = 0
    num = 0
    while sum < 100:
        sum = sum + 1
        num += sum
    print(num)
using_while()

print() 
#1b
# modifying the summation to start from 5
def main():
    sum = 0
    for i in range (5,100+1):
        sum = sum + i
    print(sum)
main()

def using_while ():
    sum = 0
    num = 5
    while num <= 100:
        sum = sum + num
        num = num + 1

    print(sum)
using_while()


print()

#1c
def main():
    sum = 0
    numb = int(input("Enter the last num:"))    
    for i in range(5,numb+ 1):
        sum = sum + i
    print(f"The sum of numbers from 5 to {numb} is {sum}")
main()
def using_while():
    sum = 0
    num = 5
    a = int(input("Enter the last num:"))
    while num <= a:
        sum += num
        num = num + 1
    print(sum+2)
using_while()

print()
#1d

    
    
    
          
        
    
