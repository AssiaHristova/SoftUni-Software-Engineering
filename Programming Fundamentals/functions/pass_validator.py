def valid_pass(password):
    count = 0
    is_valid = True
    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for symbol in password:
        if not symbol.isalpha() and not symbol.isdigit():
            is_valid = False
            print("Password must consist only of letters and digits")
            break
        if symbol.isdigit():
            count += 1
    if count < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password_1 = input()
valid_pass(password_1)
