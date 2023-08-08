#Calculator

from art import logo

def clear():
    import os
    import sys
    # Linux
    if sys.platform.startswith('linux'):
        os.system('clear')
    # Windows
    elif sys.platform.startswith('win32'):
        os.system('cls')


#Add
def add(n1,n2):
  return n1 + n2 

#Subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Devide
def divide(n1,n2):
  return n1/n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
}

def caculator():
  print(logo)
  num1 = float(input("What is the first number? : "))

  for symbol in operations:
    print(symbol)
  
  continue_calculating = True
  while continue_calculating :
    operation_symbol = input("Pick an operation : ")
  
    num = float(input("What is the next number? : "))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num)
    
    print(f"{num1} {operation_symbol} {num} = {answer}")
  
    result = input(f"Type 'y' to continue calculating {answer}, type 'n' to start a new calculation, type 'e' to exit : ")
  
    if result == 'n':
      continue_calculating = False
      clear()
      caculator()
    elif result == 'e':
      return
    else :
      num1 = answer

caculator()


