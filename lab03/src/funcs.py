def linear_search(arr, elem):
    res = -1
    for i in range(len(arr)):
        if elem == arr[i]:
            res = i
            return res
    return res


def bin_search(arr, elem):
    pairs = list(enumerate(arr))
    pairs.sort(key=lambda x: x[1])
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if pairs[m][1] == elem:
            return pairs[m][0]
        elif pairs[m][1] < elem:
            l = m + 1
        else:
            r = m - 1
    return -1
