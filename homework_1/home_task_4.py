text = input('Enter text: ')

vowel = set('qwrtpsdfghjklzxcvbnm')

for word in text:
    if vowel & set(word):
        print(word)
