name = input("Whats your name ?")
age = int(input("How old are your ?"))
tall = float(input("How tall are your ?"))
weight = float(input("Whats your weight ?"))
civil_status = int(input("1 - Married \n 2 - Single"))

if civil_status == 1:
    civil_status = True
else:
    civil_status = False

me = [name, age, tall, weight, civil_status]

print("Name: ", me[0])
print("Age: ", me[1])
print("Height: ", me[2], "m")
print("Weight: ", me[3], "kg")
print("Married: ", me[4])
