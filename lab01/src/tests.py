from funcs import *
import Levenshtein
from pyxdameraulevenshtein import damerau_levenshtein_distance
from faker import Faker

fake = Faker()

words = []
for i in range(1, 10):
    words.append(''.join(fake.random_letters(i)))
print("generated")
print("__________________________________\n")
print("Levenshtein")
print("__________________________________")
for i in range(len(words)):
    for j in range(i, len(words)):
        res = []
        for alg in (Levenshtein.distance, t_matrix_levenstein, t_recurs_levenstein, t_memo_levenstein):
            res.append(alg(words[i], words[j]))
        for k in range(1, len(res)):
            if res[0] != res[k]:
                print(f"test[{i}][{j}] went wrong")
                break
    print("for", len(words[i]), "- lettered word checked")
print("__________________________________\n")
print("Damerau-Levenshtein")
print("__________________________________")
for i in range(len(words)):
    for j in range(i, len(words)):
        res = []
        for alg in (damerau_levenshtein_distance, t_damerau_levenstein):
            res.append(alg(words[i], words[j]))
        if res[0] != res[1]:
            print(f"test[{i}][{j}] went wrong")
    print("for", len(words[i]), "- lettered word checked")