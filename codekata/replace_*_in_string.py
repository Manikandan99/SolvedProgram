m1=input()
m2=list(m1)
if(len(m1)%2==0):
  m2[((len(m2)//2)-1)]='*'
  m2[(len(m1)//2)]='*'
else:
  m2[(len(m1)//2)]='*'
print(''.join(m2))
