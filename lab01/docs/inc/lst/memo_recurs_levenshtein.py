def memo_recurs_levenstein(memo, str1, str2, i=0, j=0):
    if (i, j) in memo:
        pass
    elif len(str1) == i and len(str2) == j:
        memo[(i, j)] = 0
        return 0
    elif len(str1) == i:
        memo[(i, j)] = len(str2) - j
        return len(str2) - j
    elif len(str2) == j:
        memo[(i, j)] = len(str1) - i
        return len(str1) - i
    else:
        del_res = 1 + memo_recurs_levenstein(memo, str1, str2, i + 1, j)
        add_res = 1 + memo_recurs_levenstein(memo, str1, str2, i, j + 1)
        if str1[i] == str2[j]:
            chng_res = memo_recurs_levenstein(memo, str1, str2, i + 1, j + 1)
        else:
            chng_res = 1 + memo_recurs_levenstein(memo, str1, str2, i + 1, j + 1)
        memo[(i, j)] = min(del_res, add_res, chng_res)
    return memo[(i, j)]


def memo_levenstein(str1, str2):
    memo = {}
    return memo_recurs_levenstein(memo, str1, str2)