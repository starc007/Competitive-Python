#Memoization Solution

def fib(n):
    memo = [-1]*(n+1)
    return helper(n,memo)
def helper(n,memo):
    if memo[n]>=0: 
        return memo[n]
    if n<=2 : 
        return 1
    res = helper(n-1,memo)+helper(n-2,memo)
    memo[n] = res
    return res

print(fib(100))