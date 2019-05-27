def mergeSort(arr):
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    i =j =k =0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j +=1



arr = [23,44,66,33,55,43,22,66,88,33,55,74,24,55]

