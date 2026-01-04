import math
import random

#Functions
def calcCube():
    print("Cube side: "+str(random1))
    vol_cube=math.pow(random1,3)
    print("Volume of cube: " + str(vol_cube))

def calcRect():
    print("Rectangular box dimensions (LxWxH): "+str(random2)+" x "+ str(random3)+" x "+str(random4))
    print("Volume of rectangular box: "+str(random2 * random3 * random4))

def calcCyl():
    print("Cylinder radius: "+str(random5)+", height: "+ str(random6))
    vol_cylinder=float(math.pi * (random5 ** 2) * random6)
    print("Volume of cylinder: "+str(vol_cylinder))

def calcSphere():
    print("Sphere radius: "+str(random7))
    vol_sphere= ((4/3)* math.pi * math.pow(random7,3))
    print("Volume of sphere: "+str(vol_sphere))

#Main

random1=int(random.randint(5,7))
random2=int(random.randint(5,7))
random3=int(random.randint(5,7))
random4=int(random.randint(5,7))
random5=int(random.randint(5,7))
random6=int(random.randint(5,7))
random7=int(random.randint(5,7))

print("********************************")
print("Welcome to the Volume Calculator")
print("********************************\n")

print("Choose a shape to calculate the volume: \n1. Cube\n2. Rectangular Box\n3. Cylinder\n4. Sphere")
choice=int(input("Enter your choice (1-4): "))
if choice == 1:
    calcCube()
elif choice == 2:
    calcRect()
elif choice == 3:
    calcCyl()
elif choice == 4:
    calcSphere()
else:
    print("Invalid choice. Please select a number between 1 and 4.")