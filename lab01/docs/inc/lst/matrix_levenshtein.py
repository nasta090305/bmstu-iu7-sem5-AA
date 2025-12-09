def matrix_levenstein(str1, str2):
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