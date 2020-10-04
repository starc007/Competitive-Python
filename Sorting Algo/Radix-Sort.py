def get_digit(n, d):
  for i in range(d):
    n //= 10
  return n % 10

def digitCount(n):
  if n==0: return 1
  i = 0
  while n > 0:
    n //= 10
    i += 1
  return i
def mostDigits(nums):
    maxDigit = 0
    for i in range(len(nums)):
        maxDigit = max(maxDigit, digitCount(nums[i]));
    return maxDigit    
def radixSort(arr):
    maxDigitCount = mostDigits(arr)
    for k in range(maxDigitCount):
        digitBuckets = [ [] for j in range(10) ]
        for i in range(len(arr)):
            digit = get_digit(arr[i],k)
            digitBuckets[digit].append(arr[i])
         
        arr = []
        for sublist in digitBuckets:
            for item in sublist: 
                arr.append(item)  
                
    return arr
print(radixSort([23,345,5467,12,2345,9852]))  