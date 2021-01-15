# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

action = input("Operation to perform (+, -, *, /)")
num1 = int(input("Enter first number"))
num2 = int(input("Enter Second number"))
if (num1==45 and num2==3 and action=='*') or (num1==3 and num2==45 and action=='*'):
    print(555)
elif (num1==56 and num2==9 and action=='+') or (num1==9 and num2==56 and action=='+'):
    print(77)
elif (num1==56 and num2==6 and action=='/') or (num1==6 and num2==56 and action=='/'):
    print(4)
elif action=='+':
    print(num1+num2)
elif action=='*':
    print(num1*num2)
elif action=='/':
    print(num1/num2)
elif action=='-':
    print(num1-num2)