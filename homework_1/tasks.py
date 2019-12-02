# У вас есть массив чисел. Напишите три функции, которые вычисляют сумму этих чисел: с for-циклом,
# с while-циклом, с рекурсией.
#
# =====================================================================
#sum for
from builtins import len

lst = [1,234,345,567,345,456,-345,234,-45]
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
