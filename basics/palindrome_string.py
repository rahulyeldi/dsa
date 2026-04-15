def is_palindrome(str, start, end):
  if start>=end:
    return True
  if str[start]!=str[end]:
    return False
  return is_palindrome(str, start+1, end-1)


str = "mom"
print(is_palindrome(str, 0, len(str)-1)
