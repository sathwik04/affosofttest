x=input("enter name:")
d=len(x)
print(d)
k=2*d -2
for y in range(0,d):
    for v in range(0,k):
        print(end=" ")
    for v in range (0,y+1):
        print(x[v],end=" ")
    k=k-2
    print("\r")