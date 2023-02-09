# BMI = weight(kg)/height**2
# example input -> weight = 80, height = 1.75

height = input("Enter height in m: ")
weight = input("Enter weight in Kg: ")

bmi = int(weight)/float(height)**2
bmi_as_int = int(bmi)

print(bmi_as_int)

# 2nd methode
weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int/height_as_float**2
# or bmi = weight_as_int/(height_as_float)*(height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)