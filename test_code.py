

operation = (input("please enter an operation the choices are multiplication,division,addition,subtraction but only add the first letter of the operation:"))

number1 =  int(input("Enter your first number :"))
number2 = int(input("Enter your second number number :"))

M = number1 * number2
S = number1 - number2
D = number1 / number2
A = number1 + number2

if operation ==  'A':
    print ("The addition of your numbers is : %s" % (A))
elif operation == 'S':
    print ("The subtraction of your numbers is : %s" % (S))
elif operation == 'D':
    print ("The Division of your numbers is : %s" % (D))
elif operation == 'M':
    print ("The multiplication of your numbers is : %s" % (M))






