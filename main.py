
# ******************************
# Make your Code
# ******************************
import random
x=0
numbers1 = []
numbers2 = []
result = []
for i in range(10):
	numbers1.append(random.randint(0,10))
	numbers2.append(random.randint(0,10))
while x<10:
	result.append(numbers1[x]+numbers2[x])
	x=x+1
print (numbers1)
print (numbers2)
print(result)
