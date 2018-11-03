import pdb
x = [1,2,3]
y = 4
z = 5

result = y + z
print(result)

pdb.set_trace()

result2 = x + result# here it will error - TypeError: can only concatenate list (not "int") to list
print(result2)