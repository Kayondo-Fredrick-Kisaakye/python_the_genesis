motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

#this is an example of an INDEX ERROR

"""
Traceback (most recent call last):
  File "C:\Sr DYK\PyCharmMiscProject\learningpy1\LISTS\modifing_add_remove_elmnts\organising_list\avoid_index_errs_in_lists\avoid_index_errs_lists.py", line 2, in <module>
    print(motorcycles[3])
IndexError: list index out of range
"""

#because of  the off by one nature of indexing in lists, this is error
#An INDEX ERROR means Python cannot find an item at requested index
#keep in mind that if u want to access the last item in a list you should use INDEX -1
#this will work even if your list has changed size since the last time u accessed it