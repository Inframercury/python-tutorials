def bounded_repeater(value, max_repeats):
    for _ in range(max_repeats):
        yield value

for i in bounded_repeater("Hello", 5):
    print(i)


iterator = ('hello' for i in range(3))
print(type(iterator))
for i in iterator:
    print(i)
for i in ('hello' for i in range(3)):
    print(i)


# generators chains
def integers():
    for i in range(1, 9):
        yield i

def squared(seq):
    for i in seq:
        yield i * i

chain = squared(integers())
print(list(chain))
