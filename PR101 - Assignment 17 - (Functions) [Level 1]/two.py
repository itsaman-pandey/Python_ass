# Find max
def max(a):
    max = arr[0]
    for i in arr:
        if i>max:
            max = i
    return max

arr = [15, 2, 34, 8, 19]
print('maximum is',max(arr))