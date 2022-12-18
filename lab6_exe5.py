def valid_squareroot():
    x = int(input("Enter the number for SquareRoot:"))

    while x<0:
        print("Number cannot be negative...")
        x = int(input("Enter the number for squareroot:"))
    print(f"The squareroot of,{x}, is, {x**0.5}")
valid_squareroot()