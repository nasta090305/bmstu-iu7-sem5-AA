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
