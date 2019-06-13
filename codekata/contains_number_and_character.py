import re
m1=input()
if((bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', m1)))):
  print("Yes")
else:
  print("No")
