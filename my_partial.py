from functools import partial

def multiply(x,y):
        print("x=%d, y=%d"%((x,y)))
	return x*y

dbl = partial(multiply, 2)
print dbl(4)


