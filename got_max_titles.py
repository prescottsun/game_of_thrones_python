from pprint import pprint
from characters import characters

most_titles_count = 0
most_titles_name = ''
for character in characters:
    if len(character['titles']) > most_titles_count:
        most_titles_count = len(character['titles'])
        most_titles_name = character['name']
pprint('%s has the most titles.' % (most_titles_name))