import math

# simple calculator
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
def square(a):
    return a**2
def cube(a):
    return a**3
def square_root(a):
    return a**0.5
def cube_root(a):
    return a**(1/3)
def absolute(a):
    return abs(a)
def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
def log(a):
    return math.log(a)
def log10(a):
    return math.log10(a)
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def sinh(a):
    return math.sinh(a)
def cosh(a):
    return math.cosh(a)
def tanh(a):
    return math.tanh(a)
def asin(a):
    return math.asin(a)
def acos(a):
    return math.acos(a)
def atan(a):
    return math.atan(a)
def asinh(a):
    return math.asinh(a)
def acosh(a):
    return math.acosh(a)
def atanh(a):
    return math.atanh(a)
def degrees(a):
    return math.degrees(a)
def radians(a):
    return math.radians(a)
def pi():
    return math.pi
print("Welcome to the calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square")
print("7. Cube")
print("8. Square Root")
print("9. Cube Root")
print("10. Absolute")
print("11. Factorial")
print("12. Log")
print("13. Log10")
print("14. Sin")
print("15. Cos")
print("16. Tan")
print("17. Sinh")
print("18. Cosh")
print("19. Tanh")
print("20. Asin")
print("21. Acos")
print("22. Atan")
print("23. Asinh")
print("24. Acosh")
print("25. Atanh")
print("26. Degrees")
print("27. Radians")
print("28. Pi")
print("29. Exit")
while True:
    #take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29): ")
    #check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'):
        num1 = float(input("Enter first number: "))
        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'):
            if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27'):
                num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "**", num2, "=", power(num1, num2))
        elif choice == '6':
            print(num1, "**2", "=", square(num1))
        elif choice == '7':
            print(num1, "**3", "=", cube(num1))
        elif choice == '8':
            print(num1, "**0.5", "=", square_root(num1))
        elif choice == '9':
            print(num1, "**(1/3)", "=", cube_root(num1))
        elif choice == '10':
            print("abs(", num1, ")", "=", absolute(num1))
        elif choice == '11':
            print(num1, "!", "=", factorial(num1))
        elif choice == '12':
            print("log(", num1, ")", "=", log(num1))
        elif choice == '13':
            print("log10(", num1, ")", "=", log10(num1))
        elif choice == '14':
            print("sin(", num1, ")", "=", sin(num1))
        elif choice == '15':
            print("cos(", num1, ")", "=", cos(num1))
        elif choice == '16':
            print("tan(", num1, ")", "=", tan(num1))
        elif choice == '17':
            print("sinh(", num1, ")", "=", sinh(num1))
        elif choice == '18':
            print("cosh(", num1, ")", "=", cosh(num1))
        elif choice == '19':
            print("tanh(", num1, ")", "=", tanh(num1))
        elif choice == '20':
            print("asin(", num1, ")", "=", asin(num1))
        elif choice == '21':
            print("acos(", num1, ")", "=", acos(num1))
        elif choice == '22':
            print("atan(", num1, ")", "=", atan(num1))
        elif choice == '23':
            print("asinh(", num1, ")", "=", asinh(num1))
        elif choice == '24':
            print("acosh(", num1, ")", "=", acosh(num1))
        elif choice == '25':
            print("atanh(", num1, ")", "=", atanh(num1))
        elif choice == '26':
            print("degrees(", num1, ")", "=", degrees(num1))
        elif choice == '27':
            print("radians(", num1, ")", "=", radians(num1))
        elif choice == '28':
            print("pi()", "=", pi())
        elif choice == '29':
            break
    else:
        print("Invalid Input")

