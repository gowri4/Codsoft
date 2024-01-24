#Simple Calculator using python(function)

#declaring a function
def add(a, b):
    return a + b
def subtract(a, b):
   return a-b
def multiply(a, b):
    return a* b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Zero cannot be divided."
def percentage(a,b):
    return (a*b)/100
def exponentiation(a,b):
    return a**b
    
#check the condition for given input
while True:
    number1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /,%,**): ")
    number2 = float(input("Enter second number: "))
    if operator == '+':
        result = add(number1, number2)
    elif operator == '-':
        result = subtract(number1, number2)
    elif operator == '*':
        result = multiply(number1, number2)
    elif operator == '/':
        result = divide(number1, number2)
    elif operator == '%':
        result=percentage(number1, number2)
    elif operator == '**':
        result=exponentiation(number1,number2)
    else:
        print("Invalid operator.")
        continue

#displaying the result
    print(f"Result: {result}\n")
    print(f"Explanation for the result: {number1}{operator}{number2} = {result}\n")
    
    