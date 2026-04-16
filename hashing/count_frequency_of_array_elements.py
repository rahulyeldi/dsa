# Using Dictionary
arr = [1,2,2,1,3,4,5]
freq = {}
for i in arr:
  if i in freq:
    freq[i]+=1
  else
    freq[i]=1
print(freq)

# Fixed Size Hashing
arr = [1, 2, 2, 3, 4, 1]
hash_table = [0] * 10
for i in arr:
    hash_table[i] += 1
print(hash_table)
