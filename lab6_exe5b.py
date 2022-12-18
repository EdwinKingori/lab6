def enter_password():
    x = input("Enter Password: ")

    while len(x) <= 5:
        print("Error! Password must be more than 5 characters!")
        x = input("Enter Password: ")
    print("Sucess! Your password is set!")
enter_password()
