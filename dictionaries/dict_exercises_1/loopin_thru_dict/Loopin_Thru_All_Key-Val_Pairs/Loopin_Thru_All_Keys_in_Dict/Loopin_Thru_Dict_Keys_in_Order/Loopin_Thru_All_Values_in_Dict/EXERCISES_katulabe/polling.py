poll_guys_list = ['eric', 'john', 'phil', 'fred', 'rinah', 'james', 'kevin', 'luke', 'ken', 'julio']

poll_guys_dict = {
    'eric':'python',
    'john':'cpp',
    'phil':'c',
    'fred':'java',
    'rinah':'python',
    'james':'javascript',
    'kevin':'kotlin',
}

for poll_guy in poll_guys_dict.keys():
    print(poll_guy + " thank you for taking our poll.")
    
if 'luke' not in poll_guys_dict.keys():
    print("luke, come take the poll!")
    
if 'ken' not in poll_guys_dict.keys():
    print("ken, come take the poll!")
    
if 'julio' not in poll_guys_dict.keys():
    print("julio, come take the poll!")