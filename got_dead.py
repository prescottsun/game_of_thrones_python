from pprint import pprint
from characters import characters

dead_characters = 0
for character in characters:
    if character['died'] != '':
        dead_characters += 1
pprint('There are %s dead characters' % (dead_characters))