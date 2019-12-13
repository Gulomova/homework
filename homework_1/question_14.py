# Question 14

word = input()
upper, lower = 0, 0

for i in word:
    if 'a' <= i <= 'z':
        lower+=1
    if 'A' <= i <= 'Z':
        upper+=1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))
