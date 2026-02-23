print("Bus Pass")
name = input("Enter name: ")
age = int(input("Enter age: "))
if age < 18:
    fare = 0
else:
    fare = 500
print("Name:", name)
print("Fare:", fare)
for i in range(3):
    print("Issued")
print("End")
