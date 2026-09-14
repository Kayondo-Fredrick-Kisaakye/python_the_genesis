words = {
    'index':'like the exact spot sth is at in a list',
    'tuple':'structure you cannot change its contents',
    'indentation':'like how code is spaced or written',
    'key-value pair':'how stuff in a  dictionary is saved',
    'dyk':'one of the best programmers in uganda',
}

for word, meaning in words.items():
    print("Word: " + word.title())
    print("Meaning: " + meaning.title())

words['print'] = 'this means to display'
words['loop'] = 'this means to go through'
words['haha'] = 'at this point you know im out of words'

print("\nAFTER ADDING")
for word, meaning in words.items():
    print("Word: " + word.title())
    print("Meaning: " + meaning.title())