# Find Min
def min(a):
    min = arr[0]
    for i in arr:
        if i<min:
            min = i
    return min

arr = [15, 2, 34, 8, 19]
print('Minimum is',min(arr))

