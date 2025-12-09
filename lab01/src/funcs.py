def matrix_levenstein(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n
    cur_row = [i for i in range(n + 1)]
    print("Матрица работы алгоритма:")
    print("   ", end=' ')
    for let in str1:
        print(let, end=' ')
    print()
    print(" ", end=' ')
    for i in range(1, m + 1):
        for el in cur_row:
            print(el, end=' ')
        print()
        print(str2[i - 1], end=' ')
        prev_row, cur_row = cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            if str1[j - 1] != str2[i - 1]:
                add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1] + 1
            else:
                add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
            cur_row[j] = min(add, delete, change)
    for el in cur_row:
        print(el, end=' ')
    print()
    return cur_row[n]


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


def memo_recurs_levenstein(memo, str1, str2, i=0, j=0):
    if (i, j) in memo:
        return memo[(i, j)]
    if len(str1) == i and len(str2) == j:
        memo[(i, j)] = 0
        return 0
    if len(str1) == i:
        memo[(i, j)] = len(str2) - j
        return len(str2) - j
    if len(str2) == j:
        memo[(i, j)] = len(str1) - i
        return len(str1) - i
    del_res = 1 + memo_recurs_levenstein(memo, str1, str2, i + 1, j)
    add_res = 1 + memo_recurs_levenstein(memo, str1, str2, i, j + 1)
    if str1[i] == str2[j]:
        chng_res = memo_recurs_levenstein(memo, str1, str2, i + 1, j + 1)
    else:
        chng_res = 1 + memo_recurs_levenstein(memo, str1, str2, i + 1, j + 1)
    memo[(i, j)] = min(del_res, add_res, chng_res)
    return min(del_res, add_res, chng_res)


def memo_levenstein(str1, str2):
    memo = {}
    return memo_recurs_levenstein(memo, str1, str2)


def damerau_levenstein(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n
    prev_row = [i for i in range(n + 1)]
    print("Матрица работы алгоритма:")
    print("   ", end=' ')
    for let in str1:
        print(let, end=' ')
    print()
    print(" ", end=' ')
    for el in prev_row:
        print(el, end=' ')
    print()
    cur_row = [1] + [0] * n
    for j in range(1, n + 1):
        if str1[j - 1] != str2[0]:
            add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1] + 1
        else:
            add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
        cur_row[j] = min(add, delete, change)

    for i in range(2, m + 1):
        print(str2[i - 2], end=" ")
        for el in cur_row:
            print(el, end=' ')
        print()
        prev_prev_row, prev_row, cur_row = prev_row, cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            if str1[j - 1] != str2[i - 1]:
                add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1] + 1
            else:
                add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
            cur_row[j] = min(add, delete, change)
            if j > 1 and str1[j - 1] == str2[i - 2] and str1[j - 2] == str2[i - 1]:
                cur_row[j] = min(cur_row[j], prev_prev_row[j - 2] + 1)
    print(str2[m - 1], end=' ')
    for el in cur_row:
        print(el, end=' ')
    print()
    return cur_row[n]


def t_matrix_levenstein(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n
    cur_row = [i for i in range(n + 1)]
    for i in range(1, m + 1):
        prev_row, cur_row = cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            if str1[j - 1] != str2[i - 1]:
                add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1] + 1
            else:
                add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
            cur_row[j] = min(add, delete, change)
    return cur_row[n]


def t_recurs_levenstein(str1, str2, i=0, j=0):
    if len(str1) == i and len(str2) == j:
        return 0
    if len(str1) == i:
        return len(str2) - j
    if len(str2) == j:
        return len(str1) - i
    del_res = 1 + t_recurs_levenstein(str1, str2, i + 1, j)
    add_res = 1 + t_recurs_levenstein(str1, str2, i, j + 1)
    if str1[i] == str2[j]:
        chng_res = t_recurs_levenstein(str1, str2, i + 1, j + 1)
    else:
        chng_res = 1 + t_recurs_levenstein(str1, str2, i + 1, j + 1)
    return min(del_res, add_res, chng_res)


def t_memo_recurs_levenstein(memo, str1, str2, i=0, j=0):
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
        del_res = 1 + t_memo_recurs_levenstein(memo, str1, str2, i + 1, j)
        add_res = 1 + t_memo_recurs_levenstein(memo, str1, str2, i, j + 1)
        if str1[i] == str2[j]:
            chng_res = t_memo_recurs_levenstein(memo, str1, str2, i + 1, j + 1)
        else:
            chng_res = 1 + t_memo_recurs_levenstein(memo, str1, str2, i + 1, j + 1)
        memo[(i, j)] = min(del_res, add_res, chng_res)
    return memo[(i, j)]


def t_memo_levenstein(str1, str2):
    memo = {}
    return t_memo_recurs_levenstein(memo, str1, str2)


def t_damerau_levenstein(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n
    prev_row = [i for i in range(n + 1)]
    cur_row = [1] + [0] * n
    for j in range(1, n + 1):
        if str1[j - 1] != str2[0]:
            add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1] + 1
        else:
            add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
        cur_row[j] = min(add, delete, change)

    for i in range(2, m + 1):
        prev_prev_row, prev_row, cur_row = prev_row, cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            if str1[j - 1] != str2[i - 1]:
                add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1] + 1
            else:
                add, delete, change = prev_row[j] + 1, cur_row[j - 1] + 1, prev_row[j - 1]
            cur_row[j] = min(add, delete, change)
            if j > 1 and str1[j - 1] == str2[i - 2] and str1[j - 2] == str2[i - 1]:
                cur_row[j] = min(cur_row[j], prev_prev_row[j - 2] + 1)
    return cur_row[n]



