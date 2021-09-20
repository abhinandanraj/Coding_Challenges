def power(n,r):
  
    # if power is 0 then return 1
    if r == 0:
        return 1
    if n == 0:
        return 0
    return (n*power(n, r-1))
  
# Driver program
n = int(input())
r = int(input())
  
print(power(n, r))
