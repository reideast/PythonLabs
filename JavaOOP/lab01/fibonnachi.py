t1 = 0
t2 = 1
nextTerm = 0

n = int(input("Please input a positive integer: "))

print(t1)
print(t2)
nextTerm = t1 + t2

while (nextTerm < n):
    print(nextTerm)
    t1 = t2
    t2 = nextTerm
    nextTerm = t1 + t2