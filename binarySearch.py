def binarySearch (arr, low, high, key):
    if high >= low:
        middle = low +(high-low)//2
        if(arr[middle] == key):
            return middle
        elif(key < arr[middle]):
            return binarySearch(arr, 0, middle-1, key)
        else:
            return binarySearch(arr, middle+1, high, key)
    else:
        return -1





a = [1,2,3,4,5,6,7,8,9]
high = len(a) -1
low = 0
key = 11

result = binarySearch(a, low, high, key)
if (result != -1):
    print("key found at index %d", result)
else:
    print(key,"Key not present in array ")

