ab=input("").split()
a=int(ab[0]); b=int(ab[1])
c=int(input(""))
b+=c
hour=b//60; min=b%60
a+=hour; b=min
print(a%24,b)
