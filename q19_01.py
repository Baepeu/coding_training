# BMI 공식 : 체중(kg) / 키(m)의 제곱

weight = input("Your Weight: ")
height = input("Your Height: ")

weight = float(weight)
height = float(height)

bmi = weight / ((height/100) ** 2)

print(f"Your BMI is {bmi:.2f}.")
if bmi < 18.5:
    print("Your are underweight. You should see your doctor.")
elif bmi < 25:
    print("You are within the ideal weight range.")
else:
    print("Your are overweight. You should see your doctor.")