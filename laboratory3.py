#input of amount purchased
first = float(input("Enter the amount of your first purchase: "))   
second = float(input("Enter the amount of your second purchase: "))
third = float(input("Enter the amount of your first purchase: "))
#amount
total = first + second + third
print("Total Purchased", total)

#discount if the amount is higher than 100
if(total > 100): 
   print("You are qualified for a discout.")
   discount = total * 0.10
   new_total = total - discount
   print("New total:", new_total)

   #amount of points earned base on the total
   points =  new_total / 10.0
   print("Loyalty Points Earned:", points)

   payment = float(input("Enter your payment: "))
   change = payment - new_total
   #payment
   if(payment >= new_total): 
     print("Change: ", change)
   else:
     print("Payment Failed")
else:
   print("You are not qualified for a discout.")
   print("New total:", total)

   #amount of points earned base on the total
   points =  total / 10.0
   print("Loyalty Points Earned:", points)
    
   #payment
   payment = float(input("Enter your payment: "))
   change = payment - total
   if(payment >= total): 
     print("Change: ", change)
   else:
     print("Payment Failed")