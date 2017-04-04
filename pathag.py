from math import sqrt

print("this is a pathagoriam calculator!")
print("assume the sides are a, b, and c and c is the hypotnuse (long side of the tirangle)")
formula = input("for which side of the triangle do you want to solve? a,b,or c?")

if formula == 'c':
    sideA = int(input("enter the value of side a: "))
    sideB = int(input("enter the value of side b:"))
    sideC = sqrt(sideA * sideA + sideB * sideB)
    print("the value of side c is...")
    print(sideC)

elif formula == 'b':
    sideA = int(input('please enter the value of side a:'))
    sideC = int(input('please enter the value of side c:'))
    sideB = sqrt((sideC * sideC)-(sideA * sideA))
    print("the value of side b is...")
    print(sideB)

elif formula == 'a':
    sideB = int(input('please enter the value of side b:'))
    sideC = int(input('please enter the value of side c: '))
    sideA = sqrt((sideC * sideC)-(sideB * sideB))
    print('the value of side a is...')
    print(sideA)

else:
    print('please slect either a side from a , b ,or c')
