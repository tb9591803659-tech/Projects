#Smart calculater interface as terminal runs in loop

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
  

#Now a terminal interface


while True :

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

 elif exp.lower() == "exit" :
    print("Exiting Calculater....")
    break
 
 else:
    print("Invalid Expression!\nTry Again...")
 print("Final Result = ",result)







