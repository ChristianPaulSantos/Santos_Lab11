name=(input("Enter your name: "))
print("Choose the type of conversion: \n 1. Celsuis to Fahrenheit \n 2. Fahrenheit to Celsuis")
choice=float(input("Enter 1 or 2: "))
if(choice == 1):
    fahrenheit=float(input("Enter temperature in Fahrenhiet: "))
    C = ((9/5) * fahrenheit - 32 ) 
    print("Hello,", name + "!", fahrenheit,"is equal to", C)
else:
    celsuis=float(input("Enter temperature in Celsuis: "))
    F = ((5/9) * celsuis + 32 )
    print("Hello,", name + "!", celsuis,"is equal to", F)
