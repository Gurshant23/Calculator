print("CALCULATOR")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

var = int(input("What operation do you want to perform: "))

if var>4 or var<1:
    print("Invalid entry")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if var==1:
    print("Sum=",x+y)

elif var==2:
    print("Difference=",x-y)

elif var==3:
    print("Product=",x*y)

elif var==4:
    print("Divison:",x/y)

print("Thank You!")