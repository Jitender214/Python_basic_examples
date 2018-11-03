#Sometimes its important to know how long your code is taking to run or at least know if a particular line of code
#slowing down your entire project
#Python had built-in timing module to do this

import timeit
print("-".join(str(n) for n in range(100)))
print(timeit.timeit('"-".join(str(n) for n in range(100))',number=100))
print(timeit.timeit('"-".join([str(n) for n in range(100)])',number=100))

#sprint(%timeit "-".join(str(n) for n in range(100)))
