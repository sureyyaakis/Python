from collections import defaultdict

## Dictionaries
animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat',
}
animals

animals['a']
animals['d'] = 'dog'
animals

animals['a'] = 'antelope'
animals

animals.keys()

animals.values()

list(animals.keys())

animals['e']
animals.get('a')
len(animals)

animals = {
    'a': ['aardvark', 'antelope'],
    'b': ['bear'],
}
animals['b'].append('bison')
animals['c'] = ['cat']
if 'c' not in animals:
    animals['c'] = []
    
animals['c'].append('cat')


### The Default Dict
animals = defaultdict(list)
animals
animals['e'].append('elephant')
animals
animals['e'].append('emu')
animals
animals['f']
