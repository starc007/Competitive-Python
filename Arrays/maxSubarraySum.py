# SLIDING WINDOW PATTERN

n = int(input())
arr1 = list(map(int,input().split()))

def maxSubarraySum(arr,num):
    maxSum = 0
    tmpSum = 0
    if(len(arr) < num): return None
    for i in range(0,len(arr)):
        maxSum += arr[i]
    tmpSum  = maxSum
    j = 0
    while(j<len(arr)):
        tmpSum = tmpSum - arr[j-num] + arr[j]
        maxSum = max(maxSum, tmpSum)
        j+=1

    return maxSum

print(maxSubarraySum(arr1,n))        

