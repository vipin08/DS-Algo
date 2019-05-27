def interplotationSearch(arr, n, x):
    low_index, high_index = 0, n-1
    while high_index >= low_index and x <= arr[high_index] and x >= arr[low_index]:
        if low_index == high_index:
            if arr[low_index] == x:
                return low_index
            return -1
        pos = low_index + int(float((high_index-low_index)/(arr[high_index]-arr[low_index]))*(x-arr[low_index]))
        if arr[pos] == x:
            return pos
        if arr[pos] > x:
            high_index = pos - 1
        if arr[pos] < x:
            low_index = pos + 1
    return -1
array = [1,2,3,4,5,6,7,8,9,11,23,33,44,55,66,77,88,99,100]
x = 55
n = len(array)

result = interplotationSearch(array, n, x)
if result == -1:
    print("Value not found in array")
else:
    print("value found on =>", result)
