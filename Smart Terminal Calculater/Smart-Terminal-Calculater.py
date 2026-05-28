#Smart calculater interface as terminal runs in loop
import os

def add(a , b):
    return a + b
def sub(a , b):
    return a - b
def mul(a , b):
    return a * b
def div(a,b) : 
    if b == 0 :
        return None
    else :
        return a / b
    
def history_add(expression) :
      with open("history.txt","a") as file :
         file.write(expression + "\n")


#Now a terminal interface
print("CALCULATER\n")
while True :
   print("1.Calculate\n2.View History\n3.Exit")
   option = int(input("Enter any option: "))
   if option == 1:
      exp = str(input("Enter Expression: "))

      if "+" in exp :
         parts = exp.split("+")
         result = add(float(parts[0]),float(parts[1]))

      elif "-" in exp:
         parts = exp.split("-")
         result = sub(float(parts[0]),float(parts[1]))

      elif "*" in exp :
         parts = exp.split("*")
         result = mul(float(parts[0]),float(parts[1]))

      elif "/" in exp:
         parts = exp.split("/")
         if float(parts[1]) == 0 :
            print("Error: not able to divide by zero")
            continue
         result = div(float(parts[0]),float(parts[1]))
      
      else:
         print("Invalid Expression!\nTry Again...")
         continue
      history_add(exp)
      print("Final Result = ",result)
   
   elif option == 2:
      if os.path.exists("history.txt") : 
         with open("history.txt","r") as file: 
            for line in file : 
               print(line.strip())
      else :
         print()

   elif option == 3:
      print("Exiting Calculater...\nExited Calculater.")
      break

   else :
      print("Invalid option...\nTry again.")





