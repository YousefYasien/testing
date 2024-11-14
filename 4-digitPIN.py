from string import digits
from itertools import product
for i in product(digits,repeat=4):
    print(*i)