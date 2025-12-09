def recurs_levenstein(str1, str2, i=0, j=0):
    if len(str1) == i and len(str2) == j:
        return 0
    if len(str1) == i:
        return len(str2) - j
    if len(str2) == j:
        return len(str1) - i
    del_res = 1 + recurs_levenstein(str1, str2, i + 1, j)
    add_res = 1 + recurs_levenstein(str1, str2, i, j + 1)
    if str1[i] == str2[j]:
        chng_res = recurs_levenstein(str1, str2, i + 1, j + 1)
    else:
        chng_res = 1 + recurs_levenstein(str1, str2, i + 1, j + 1)
    return min(del_res, add_res, chng_res)