#'python' and 'python ' aren't the same
#the interpreter detects the extra space as significant unless you tell it otherwise
#it's important to think about whitespace, you'll often wnt to compare 2 strings to determine
#whether they're the same
#forexample: one might ccontain checking peopl's usernames while logging into a website

#python can see them on right and left
#on the right side>>> use = rstrip() method:
     #"""
#>>> favourite_language = 'python '
#>>> favourite_language
#'python '
#>>> favourite_language.rstrip()
#'python'
     #"""  #here the whitespace is removed temporarily,
          #if you ask for te value of favourite_language again, the string looks as it was entered
          #to remove it forever, u av to associate the stripped value withe variable name

"""
>>> favourite_lang = 'python '
>>> favourite_lang = favourite_lang.rstrip()
>>> favourite_lang
'python'
"""
#stripping on the >>>Right is rstrip()  >>>left is lstrip() >>> both sides is >>>strip()
