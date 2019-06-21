"""Sanakirjat ovat hyviä heterogeenisen infon varastointiin:"""

#lookup = {}
#lookup = dict()
#lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')

# HUOM: Olio-ohjelmoinnissa luokan ja olion luonnissa konstruktorilla käytetään sanakirjaa:

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

gandolf = Wizard("Gandolf", 42)

print(gandolf.__dict__)

print(lookup)
print(lookup['loc'])

#lookup['cat']

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

# Suppose these came from a data source, e.g. database, web service, etc
# And we want to randomly access them
import collections

User = collections.namedtuple('User', 'id, name, email')
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm'),
]

# Tässä sanakirjaa käytetään tiedonhakuun

lookup = dict()
for u in users:
    lookup[u.id] = u

# Tsekataampa tällä periaatteella esim. user3:

print(lookup[4])

«