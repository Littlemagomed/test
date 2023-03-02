m=int(input('m= '))
n=int(input('n= '))
for i in range(1,6):
    if n<=0 or m<=0:
        m=int(input('insert a positive quatity for m= '))
        n=int(input('insert a positive quatity for n= '))
        if i==5 and n<=0 or m<=0:
            print("Congrates, You're idiot")
            break

temp=m
#s=0
for j in range(1,n):
    s=0
    for k in range(1,m+1):
        s=s+temp
    temp=s
print(s)
