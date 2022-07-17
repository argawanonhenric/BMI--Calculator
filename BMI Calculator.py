# Get the individual's weight in pounds(lbs) and height in inches(inch)
weight = float(input("Enter your Weight(kg): "))
height = float(input("Enter your Height: "))

# Conversion
height_in_meters = height / 100

# Compute the height
h2 = height_in_meters * height_in_meters

# Calculate the BMI = w / h*2
BMI = weight / 2

# Show the individual's BMI
print('Your Body Mass Index (BMI) is: ', BMI)

# Check if the BMI is valid. The result would be invalid if the inputs are negative numbers
if BMI > 0:
  # Print the results depending on the BMI value
  if BMI < 16:
    print('You are severely underweight')
  elif BMI < 17:
    print('You are moderately underweight')
  elif BMI < 18.5:
    print('You are underweight')
  elif BMI < 25:
  	print('You are healthy')
  elif BMI < 30:
  	print('You are overweight')
  elif BMI < 35:
    print('You are moderately obese')
  elif BMI <= 40:
    print('You are severely obese')
  elif BMI > 40:
    print('You are morbidly obese')
else:
  print('The information that you put in is incorrect')