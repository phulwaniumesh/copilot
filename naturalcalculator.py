# initializing string variable
String1 = str(input("Enter complete expression: "))
print("The original string is : " + String1)
# Expression evaluation in String
# Using eval()
result1 = eval(String1)

# printing result
print("The evaluated result is : " + str(result1))