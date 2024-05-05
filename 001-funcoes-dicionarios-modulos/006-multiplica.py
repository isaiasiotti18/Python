def multi(*args):
  total = 0
  for num in args:
    if total == 0:
      total += num
      continue
    total *= num
    
  return total
  

print(multi(5,2,2,5*100))