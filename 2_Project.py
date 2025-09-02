# Basic Login System – Ask for username & password,
# allow access only if both match predefined values.


username=input("Enter Your Name : ")
passs=input("Enter Your password : ")


if(username=="ShayanHassan" and passs=="Shayan2115"):
    print("Name :",username)
    print("Password :",passs)
    print("Location : Swabi")
    print("phone_Number : +92-311 9423636")
    print("Job : Machine learning Engineer")
    print("Compnay Name : Code_Canvas")
else:
    print("Invalid Username OR Invailed Password")

