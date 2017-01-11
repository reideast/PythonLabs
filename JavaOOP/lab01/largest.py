print("Input three integers: ")
a = int(input())
b = int(input())
c = int(input())

if a >= b:
    if a >= c:
        print(str(a) + " is the largest")
    else:
        print(str(c) + " is the largest")
else:
    if b >= c:
        print(str(b) + " is the largest")
    else:
        print(str(c) + " is the largest")