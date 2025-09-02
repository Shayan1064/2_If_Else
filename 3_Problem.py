# Ask the user for age, and decide the ticket price:

# Under 12 → Rs. 100

# 12–18 → Rs. 200

# 19–60 → Rs. 300

# Above 60 → Rs. 150

age=int(input("Enter Your Age : "))
if(age<12):
    print("Your Ticket Price is 100")
elif(age>12 and age <25):
    print("Your Ticket Price is 500")
else:
    print("Your Ticeckt Price is 1000")