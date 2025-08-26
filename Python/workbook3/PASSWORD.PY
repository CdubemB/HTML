print("enter your password")

password = input()

if len(password) < 8:
     print("too short")
     exit()
else:
     print("you  have been logged in")