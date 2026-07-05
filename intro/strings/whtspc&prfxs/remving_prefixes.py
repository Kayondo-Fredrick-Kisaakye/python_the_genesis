#when working with strings, another common task is to remove a prefix
#consider a URL with a common prefix https://.
#we want to remove this prefix, so we can focus on just the URL that users need to enter
#into an address bar...heres how
"""
>>> nostarch_url = 'https://nostarch.com'
>>> nostarch_url.removeprefix('https://')
'nostarch,com'
"""

# enter the name of te variable, then a dot, then method, removeprefix()
#inside the parentheses, enter the prefix u want to remove from te original string
  #like  the methods for removing whitespace, removeprefix() leaves the original string unchanged
  #if you want to keep the new value with the prefi removed, either reassign it to the original varriable
  #or assign to  new variable

""">>> simple_url = nostarch_url.removeprefix('https://')"""
#in a browser if u see that the https:// is not shownss the browser is probably using removeprefix()
