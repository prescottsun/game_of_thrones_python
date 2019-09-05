from pprint import pprint
from characters import characters



count_A = 0
for character in characters:
    if character['name'][0] == 'A':
        count_A += 1
    # if character['name'].startswith('A') == True:
pprint('There are %s characters whose names start with A' % (count_A))

count_Z = 0
for character in characters:
    if character['name'][0] == 'Z':
        count_Z += 1
pprint('There are %s characters whose names start with Z' % (count_Z))