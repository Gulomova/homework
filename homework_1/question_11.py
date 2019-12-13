#  Question 11


def check(x):
    total, pw = 0, 1
    reversed(x)

    for i in x:
        total += pw * (ord(i) - 48)
        pw *= 2
    return total % 5


data = input().split(",")
lst = []

for i in data:
    if check(i) == 0:
        lst.append(i)

print(",".join(lst))
