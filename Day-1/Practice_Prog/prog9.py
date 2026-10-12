a=int(input())
n=a
ord=len(str(n))
s=0
while n!=0:
    r=n%10
    s+=(r**ord)
    n//=10
#print(s)
if s==a:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")