def create_multipliers():
    multipliers = []
    
    for i in range(5):
      def multiplier(x):
        return i*x
      multipliers.append(multiplier)

    return multipliers

for mul in create_multipliers():
  print mul(2)

# all 8  
