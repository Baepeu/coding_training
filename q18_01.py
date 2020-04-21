print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
menu = input("Your choice: ")
# menu = menu.upper()
if menu.upper() == "C":
    F = input("Please enter the temperature in Fahrenheit: ")
    F = float(F)
    C = (F-32) * 5/9
    print(f"The temperature in Celsius is {C}.")
elif menu.upper() == "F":
    C = input("Please enter the temperature in Celsius: ")
    C = float(C)
    F = (C*9/5)+32
    print(f"The temperature in Fahrenheit is {F}.")
else:
    print("Not exists.")