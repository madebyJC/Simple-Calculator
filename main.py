from replit import clear
from art import logo

print(logo)

user_result = ""


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  num1 = int(input("What is the first number? "))
  
  for symbol in operations:
    print(symbol)
  
  user_continue = True
  while user_continue == True:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What is the second number? "))
    user_operation = operations[operation_symbol]
    user_result = user_operation(n1=num1, n2=num2)
    
    print(f"{num1} {operation_symbol} {num2} = {user_result}")
  
    result_continue = input("Would you like to continue the calculator with the last result? Type \"yes\" or \"no.\"\n").lower()
    if result_continue == "yes":
      num1 = user_result
    else:
      user_continue = False
      clear()
      calculator()
      
calculator()
    
