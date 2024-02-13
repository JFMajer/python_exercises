import operator

PEOPLE = [
    {'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
    {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
    {'first': 'Elon', 'last': 'Musk', 'email': 'elon@spacex.com'},
    {'first': 'Ada', 'last': 'Lovelace', 'email': 'ada@analyticalengine.com'},
    {'first': 'Grace', 'last': 'Hopper', 'email': 'grace@navy.mil'}
]


def alphabetize_names():
    return sorted(PEOPLE, key=operator.itemgetter('last', 'first'))

print(alphabetize_names())
