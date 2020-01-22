# TASK №2

a = [1, 2, 5, 4]
b = [11, 22, 33]
c = a + b
c = [str(item) for item in c]
# f = []
# for item in c:
#     f.append(str(item))
c.sort()
c = [int(item) for item in c]
print(c)
