# Think of five programming words you’ve learned about in the previous
# chapters . Use these words as the keys in your glossary, and store their
# meanings as values .
# Print each word and its meaning as neatly formatted output . You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line . Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output

words = {
    'index':'like the exact spot sth is at in a list',
    'tuple':'structure you cannot change its contents',
    'indentation':'like how code is spaced or written',
    'key-value pair':'how stuff in a  dictionary is saved',
    'dyk':'one of the best programmers in uganda',
}

start_word = input("Type 'okay' to see words: ")
the_word = "okay"

if start_word == the_word:
    print("Index:\n" + str(words['index']))
    print("Tuple:\n" + str(words['tuple']))
    print("Indentation:\n" + str(words['indentation']))
    print("Key-value pair:\n" + str(words['key-value pair']))
    print("DYK:\n" + str(words['dyk']))
else:
    print("Please, follow instructions!")