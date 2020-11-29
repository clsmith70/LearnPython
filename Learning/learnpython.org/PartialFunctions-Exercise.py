#PartialFunctions-Exercise.py
from functools import partial

def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x

# create a partial function, with replaced varialbles,
# so that a value for x returns 60
mypart = partial(func,7,6,5)
print(mypart(4))
marpart2 = partial(func,6,5,4)
print(marpart2(13))