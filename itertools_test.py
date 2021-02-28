import itertools

l = ['Masha', 'Sveta', 'Olya', 'Snezhana', 'Katya']
grouped = itertools.groupby(l, key=len)
for k, g in grouped:
    print(k, list(g))
