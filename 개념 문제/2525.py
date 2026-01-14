ab=input("").split()
a=int(ab[0]); b=int(ab[1])
c=int(input(""))

hour=c//60; min=c%60
a+=hour; b+=min

if b>=60:
    a+=(b//60)
    b%=60
if a>=24:
    a%=24

print(a,b)
