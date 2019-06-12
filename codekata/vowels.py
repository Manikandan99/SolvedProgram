l=['a','e','i','o','u']
m=input()
if(l.count(m)!=0):
    print("Vowel")
elif(m.isalpha()):
    print("Consonant")
else:
    print("invalid")
