password = ""

while True:
    password = input("Enter a password: ")

    # Check if the password meets the required criteria
    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password):
        # Password meets criteria, so break out of the loop
        break
    else:
        # Password does not meet criteria, so display an error message and continue the loop
        print("Error: Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")

print("Success! Your password has been set.")
