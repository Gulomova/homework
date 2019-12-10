# TASK №1

#sum for
from builtins import len, repr

lst = [10, 20, 30, 40, 50, 60, 70]
n=0
for i in lst:
    n+=i
print(n)

#sum while
n=0
i=0
while i < len(lst):
    n+=lst[i]
    i+=1
print(n)

#sum recursion
def recursesum(lst, summ = 0):
    if lst:
        summ += lst.pop(0)
        summ = recursesum(lst, summ)
    return summ
n = recursesum(lst)
print(n)
