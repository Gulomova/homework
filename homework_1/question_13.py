#  Question 13

word = input()
letter, digit = 0, 0

for i in word:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        letter += 1
    if '0' <= i <= '9':
        digit += 1

print("LETTERS {0}\nDIGITS {1}".format(letter, digit))
