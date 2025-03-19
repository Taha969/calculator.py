while(True):
 text = ("\t welcome to my calculator" )
 print(text.upper())
 num1 = float(input("please enter the firest number: "))
 operator = input("please emter the operator: ")
 num2 = float(input("please enter the second number: "))
 if operator == "+":
    print(num1 + num2)
 elif operator == "-":
    print(num1 - num2)
 elif operator == "*":
    print(num1 * num2)
 elif operator == "/":
    print(num1 / num2)
 else:
    print("Error")
 mode = input("Enter your Mode 5 to end or enter . try again: ") #انا  عرف انو لاو ضغط على اي شيء ثاني رح يصير في ثكرر
 if mode == "5":
       exit()
       print("5. Stop.")
 elif mode == "5":
        exit()
