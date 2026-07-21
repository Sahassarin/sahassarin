#input
weight = int(input("Enter weight: "))
height = float(input("Enter height: "))

#process
BMI = weight / height ** 2

#output
print("BMI: " +str(BMI))
if BMI < 18.6 :
   print ("Underweight")
elif BMI < 23.0:
   print ("Normal weight")
elif BMI < 25.0:
   print ("Overweight")
elif BMI < 30.0:
   print ("Obesity class I")
elif BMI > 29.9:
   print ("Obesity class II")