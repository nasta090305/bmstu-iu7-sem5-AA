def linear_search(arr, elem):
    cmp = 0
    res = -1
    for i in range(len(arr)):
        cmp += 1
        if elem == arr[i]:
            res = i
            return res, cmp
    return res, cmp