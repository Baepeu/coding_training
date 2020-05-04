def passwordValidator(password):
    password_length = len(password)
    if password_length < 8 and password.isdigit():
        return 0
    elif password_length < 8 and password.isalpha():
        return 1
    elif password_length >= 8 and password.isalnum():
        return 2
    elif password_length >= 8 and not password.isalnum():
        return 3
    else:
        return 0

password_level = ['very weak','weak','strong','very strong']
password = input("Enter your password: ")

password_msg = password_level[passwordValidator(password)]
msg = f"The password '{password}' is a {password_msg} password."

print(msg)
