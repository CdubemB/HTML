#Creating and using lists in python

listA = [1, 2, -3]

print(listA)
listA.append(4)# 'append' adds something to a list
print(listA)
listA.pop()# 'pop' takes the last item off a list
print(listA)

print(listA[0])

listA[0] = 100 #Changing the values of list A
print(listA)
name = input()

listB = ["bannana", "apple", "microsoft"]

temp1 = b[0]# The variable temp1 equals bannana

b[0] = b[2]#The first item of the list is know microsoft
b[2] = temp1 #know temp1 equals bannana
#THE TEMP1 EXAMPLE IS THE SLOW WAY

b[0], b[2] = b[2], b[0]
#THIS IS THE FAST WAY