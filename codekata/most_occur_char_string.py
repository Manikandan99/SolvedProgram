import collections
s = input()
mk=collections.Counter(s).most_common(1)[0]
print(mk[0])
