n=int(input("enter a no"))
s=0
t=n
a=len(str(t))
while(t>0):
    d=t%10
    s=s+d**a
    t=t//10

if(n==s):
    print("armstrong")
else:
    print("not armstrong")
