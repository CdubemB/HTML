#LOOPS IIN PYTHON
listA = ["banana", "apple", "micorsoft"]

for element in listA:
  print(element)
  print(element)

listB = [20, 10, 5]
total = 0
for e in listB:
  total = total + e
print(total)

listC = list(range(1, 5)) # "range" will take numbers from one since it is taking the range of these numbers
total2 = 0
for i in range(1, 11):
  total2 += i# "+=" will add something to itself - it is quicker than saying total 2 = total2 + i
print(total2)

print(5 % 3)#The "%" will divide the two numbers andthen show the remainder (which should be 2)

total3 = 0

for j in range(1, 8):
  if j % 3 == 0:
    total3 += j
print(total3)
