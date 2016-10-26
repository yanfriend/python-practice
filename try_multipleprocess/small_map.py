from multiprocessing import Pool

def f(x):
    # complicated processing
    return x+1

y_serial = []
x = range(100)
for i in x: y_serial+=[f(i)]

pool = Pool()
y_parallel = pool.map(f, x) 

print y_serial == y_parallel

