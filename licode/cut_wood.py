def isValid(cutLen, arr, k):
  count = 0
  for wood in arr:
    if(wood >= cutLen):
      count += wood // cutLen
    else:
      return False
  if(count >= k):
    return True

def cutWood(wood, k):
  left = 1
  right = max(wood) + 1
  while left < right:
    middle = (left + right) // 2
    if(isValid(middle, wood, k)):
      left = middle + 1
    else:
      right = middle
  return left-1

print(cutWood(wood = [232, 124, 456], k = 7)) # 114
print cutWood(wood = [1, 2, 3], k = 7) # 0
print cutWood(wood = [5, 9, 7], k = 4) # 4
print cutWood(wood = [5, 9, 7], k = 3) # 5
