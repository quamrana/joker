"""
Write a program that asks the user which package they would like to purchase, 
and the quantity that they would like to purchase. 
The program should then display to the user the discount applicable (if any), 
and the final cost of their purchase.
You should also develop and submit the pseudocode OR flowchart for this program



Productivity sells for $110 and Efficiency sells for $180.

Quantity discounts for Productivity are as follows:
10 - 19 : 10%
20 - 49: 20%
50+ : 35% 

Quantity discounts for Efficiency are as follows:
10 - 29 : 15%
30 - 39: 20%
40+ : 35% 
"""

hello = input("Hello! What would you like to purchase today? ").upper()

if "PACKAGE" == hello:
    
    print("Ok you would like to purchase a package.")
    print("Package quantity for productivity sells at $110.")
    print("Package quanitiy for Efficiency sells for $180.")

    question = input("Would you like the purhase the quanitity of productivity or efficiency? ").lower()
    
     
    if "productivity" == question:
    
      question1 = int(input("How many items would you want ? "))
       
      discount1 = 0.10
      percentage1 = "{:.0%}".format(discount1)
      
      discount2 = 0.20
      percentage2 = "{:.0%}".format(discount2)
      
      discount3= 0.35
      percentage3 = "{:.0%}".format(discount3)
      
      if 10 <= question1 <= 19:
         print("you get a discount of", percentage1)
       
      elif 20 <= question1 <= 49:
         print("you get a discount of", percentage2)
          
      elif 50 <= question1 <= 60:
         print("you get a discount of", percentage3)
         
      elif 1 <= question1 <= 9:
          
         print("sorry you don't qualify for a discount")
         
    if "efficiency" == question:
      question2 = int(input("How many items would you want ? "))

      Discount1 = 0.15
      Percentage1 = "{:.0%}".format(Discount1)

      Discount2 = 0.20
      Percentage2 = "{:.0%}".format(Discount2)

      Discount3= 0.35
      Percentage3 = "{:.0%}".format(Discount3)

      if 10 <= question2 <= 29:
        print("you get a discount of", Percentage1)

      elif 30 <= question2 <= 39:
        print("you get a discount of", Percentage2)

      elif 40 <= question2 <= 50:
        print("you get a discount of", Percentage3)

      elif 1 <= question2 <= 9:

       print("sorry you don't qualify for a discount")
    
else:
   print("Sorry your answer is not package...Goodbye!")
