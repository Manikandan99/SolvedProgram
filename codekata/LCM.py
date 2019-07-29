from math import gcd
mk1,mk2 = map(int,input().split())
mk3=gcd(mk1,mk2)
lcm=(mk1*mk2) // mk3
print(lcm)
