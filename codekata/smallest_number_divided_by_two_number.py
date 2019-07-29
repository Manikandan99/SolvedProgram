from math import gcd
mani1,mani2 = map(int,input().split())
mk3=gcd(mani1,mani2)
harsha=(mani1*mani2) // mk3
print(harsha)
