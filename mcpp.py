#area of the circle 
import math
r=float(input("input the radius the circle : "))
print("the area of the circle with radius " + str(r) + " is: " + str(math.pi * r**2))

#file extension 
filename = input("input the filename: ")
index=0
for i in range(len(filename)):
    if filename[i]=='.':
        index=i
if(filename[index+1: ]=='py'):
    print("python")
else:
    print(filename[index+1: ])
