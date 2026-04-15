def sum_n(n):
  if n==0:
    return 0
  return n+sum(n-1)

print(sum_n(5))
