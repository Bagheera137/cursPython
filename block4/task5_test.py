from itertools import permutations
from task5 import test5

def tester(test_def, result, params):
    res = test_def(*params)
    if res != result:
        print("Ошибка теста. Даны параметры:", params, "Получен результат ", res, "вместо", result)

arr = [5, 10, 15]
for comb in permutations(arr, 3):
    print(comb)
    r=list(comb)
    r.sort()
    tester(test5,r, list(comb))