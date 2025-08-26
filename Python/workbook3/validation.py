ans=input("Please enter your name; " )
if len(ans) > 0:
	print("Thank you for entering your name")    

#look up check

ans=input("Please enter email address: " )
for i in range(len(ans)):
        if ans[i]=="@":
                print("Thank you for entering an email address which includes an @ symbol")
                #type up check
                try:
                        ans=int(input("Please enter your age: "))
                except:
                        print("Age must be a whole number please try again")
                else:
                        print("Thank you for entering your age")

#range check

ans=int(input("Please charge of your laptop"))
if ans >= 0 and ans <= 60:
	print("Thank you for entering your phone charge level")   

#divide by zero check

numOne=int(input("Enter first number: "))
numTwo=int(input("Enter second number: "))
try:
        ans=numOne/numTwo
except ZeroDivisionError:
        print("Second number cannot be zero!")
else:
        print("The answer is: ", ans)    

