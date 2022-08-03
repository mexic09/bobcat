arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def binary_search(arr, needed):
    start = 0
    end = len(arr) - 1
    mid = 0
    step = 0

    while start <= end:

        step += 1
        mid = (start + end) // 2

        print('(', arr[start], '+', arr[end], ')', '//', '2', '=', arr[mid], '\n', step)

        if needed == arr[mid]:
            return mid

        if needed < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1

#print(binary_search(arr, 2))
#print(binary_search(arr, 7))
#print(binary_search(arr, 12))
#print(binary_search(arr, 15))
print(binary_search(arr, 0))
#print(binary_search(arr, 22))