#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a / b
    except:
        return 'zero_div_err'

def power(a,b):
    return a**b

def remainder(a,b):
    return a%b


#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice == '#':
        return -1
    
    if choice == '$':
        return

    if choice not in ['+' ,'-', '*', '/', '^', '%']:
        print('Unrecognized operation')
        return
    
    operand_1 = input("Enter first number: ")
    print(operand_1)
    
    if operand_1 == '#':
        return -1
    if operand_1 == '$':
        return
    
    try:
        operand_1 = float(operand_1)
    except:
        return
    
    operand_2 = input("Enter second number: ")
    print(operand_2)
    
    if operand_2 == '#':
        return -1
    if operand_2 == '$':
        return
    
    try:
        operand_2 = float(operand_2)
    except:
        return
    
    if choice == '+':
        result = add(operand_1, operand_2)
    elif choice == '-':
        result = subtract(operand_1, operand_2)
    elif choice == '*':
        result = multiply(operand_1, operand_2)
    elif choice == '/':
        result = divide(operand_1, operand_2)
    elif choice == '^':
        result = power(operand_1, operand_2)
    else:
        result = remainder(operand_1, operand_2)
    
    if not result:
        print("Something Went Wrong")
    if result == 'zero_div_err':
        print("float division by zero")
        print(operand_1, choice, operand_2, "=", 'None')
    else:
        print(operand_1, choice, operand_2, "=", result)

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()