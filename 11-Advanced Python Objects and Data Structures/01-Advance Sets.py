s = set()
s.add(1)
s.add(2)
print(s)
s.clear()
print(s)

s1 = {1,2,3}
set_copy = s1.copy()
print(s1)
print(set_copy)
s1.add(4)
print(s1.difference(set_copy))

s2 = {1,2,3,4}
s2.discard(2)
print(s2)

#union()