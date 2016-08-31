from functools import partial
from operator import mul

def create_multipliers():
   return [ partial(mul, i) for i in range(5)]

for mul in create_multipliers():
  print mul(2)

# 0,2,4,6,8  
