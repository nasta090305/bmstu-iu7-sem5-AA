#1062 элемента
from matplotlib import pyplot as plt
print("counter")

def linear_search(arr, elem):
    cmp = 0
    res = -1
    for i in range(len(arr)):
        cmp += 1
        if elem == arr[i]:
            res = i
            return res, cmp
    return res, cmp


def bin_search(arr, elem):
    cmp = 0
    pairs = list(enumerate(arr))
    pairs.sort(key=lambda x: x[1])
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        cmp += 1
        if pairs[m][1] == elem:
            return pairs[m][0], cmp
        elif pairs[m][1] < elem:
            l = m + 1
        else:
            r = m - 1
    return -1, cmp
