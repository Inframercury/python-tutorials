from collections import namedtuple
from collections import Counter
from typing import NamedTuple

from collections import defaultdict

fs = frozenset({'a', 'b', 'c'})

Car = namedtuple('Car', 'color mileage automatic')
car1 = Car('red', 150, True)
print(car1)
