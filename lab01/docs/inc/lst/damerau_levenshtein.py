def damerau_levenstein(str1, str2):
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