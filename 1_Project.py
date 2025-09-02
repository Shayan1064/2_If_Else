# Library Fine Calculator – User enters number of late days; 
# calculate fine based on rules 
# (e.g., 1–5 days Rs. 10/day, 6–10 days Rs. 20/day, >10 days Rs. 50/day).


day=int(input("Enter Number Of Late Days : "))
fine=0
if(day>0 and day<5):
    fine=day*15
    print("You Fine is ",fine)
elif(day >5 and day <15):
    fine=day*25
    print("Your Fine is ",fine)
else:
    fine=day*50
    print("Your Fine is ",fine)