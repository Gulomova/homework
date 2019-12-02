# TASK №1
# У вас есть массив чисел. Напишите три функции, которые вычисляют сумму этих чисел: с for-циклом,
# с while-циклом, с рекурсией.
# =====================================================================

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

# TASK №2
#
# Напишите функцию, которая создаёт комбинацию двух списков таким образом:
# [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
#
# =====================================================================

def combine_lists(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        limit = len_a
    else:
        limit = len_b
    i = 0
    r = []
    while i < limit:
        r.append(a[i])
        r.append(b[i])
        i += 1
    return r

if __name__ == '__main__':
    a = ['a', 'b', 'c']
    b = ['A', 'B', 'C', 'D']
    print(repr(combine_lists(a, b)))

#TASK №3
#Вычислите первые 100 чисел Фибоначчи. (Напишите код.)
#
#=====================================================================

def fibonacci(n=10, a=0, b=1):
    yield a
    yield b
    n -= 2
    while n > 0:
        c = a + b
        a = b
        b = c
        yield c
        n -= 1

if __name__ == '__main__':
    for n in fibonacci(100):
        print(n)





