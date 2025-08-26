#TWO DIMENSIONAL ARRAYS     BY DUBEM BARDI
rowLength=9
columnLength=5
myArray=[[0 for row in range(rowLength)] for column in range(columnLength)]
print(myArray)

myArray[0][4] = 99
myArray[2][3] = 74
print(myArray)

# print out a row at a time                   
for row in range(rowLength):
		print(myArray[row])
 
