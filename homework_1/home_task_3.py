words = ['mississippi', 'miss', 'lake', 'que', '', 'rrr1']

vowel = set('qwrtyipsdfghjklzxcvbnm')

for word in words:
    if vowel & set(word):
        print("{} ".format(word)*3)


