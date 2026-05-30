#Smart calculater interface as terminal runs in loop 
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

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
   print(Fore.YELLOW + "[1]" + "Calculate")
   print(Fore.YELLOW + "[2]" + "View History")
   print(Fore.YELLOW + "[3]" + "Exit")
   print(Fore.YELLOW + "[4]" + "Delete History")
   try:
      option = int(input(Fore.BLUE  + Style.BRIGHT + "Enter any option: "))
      if option == 1:
         exp = input(Fore.BLUE  + Style.BRIGHT + "Enter Expression: ")

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
         print(Fore.GREEN  + f"Final Result = {result}")

      elif option == 2:
         if os.path.exists("history.txt") : 
            with open("history.txt","r") as file: 
               for line in file : 
                  print(Fore.WHITE + Style.BRIGHT + line.strip() + Style.RESET_ALL)
         else :
            print()

      elif option == 3:
         print(Fore.GREEN + "Exiting Calculater...\nExited Calculater.")
         break

      elif option == 4:
         pass #Has to be done and also time stamp should be added and then scientific calculation parsing system should be added

      else :
         print(Fore.RED + "Invalid option...\nTry again.")
      
   except Exception as e :
      print(e)

      #Remaining :
      #1.Scientific Calculations
      #2.Hsitory Deletion