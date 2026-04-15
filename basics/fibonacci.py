def fibonacci(n):
  if n<=1:
    return n
  return fibonacci(n-1) + fibonacci(n-1)

n=6
print(fibonacci(n))
