print("BMI Calculator!\n")
height = float(input("Height in m : "))
weight = float(input("Weight in kg : "))
bmi = weight / height ** 2
bmi = round(bmi,2)
if bmi < 18.5 :
  print(f"Your BMI is {bmi} and your are underweight")
elif 25 > bmi >= 18.5 :
  print(f"Your BMI is {bmi} and your are normalweight")
elif 30 > bmi >= 25 :
  print(f"Your BMI is {bmi} and your are slightly overweight")
elif 35 > bmi >= 30 :
  print(f"Your BMI is {bmi} and your are obese")
else:
  print(f"Your BMI is {bmi} and your are clinically obese")