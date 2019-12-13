#   Question 15

a = input()
total, tmp = 0, str()

for i in range(4):
    tmp += a
    total += int(tmp)

print(total)
