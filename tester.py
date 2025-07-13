def tester(test_def, result,*params):
    res = test_def(*params)
    if res != result:
        print("Ошибка теста. Даны параметры:", *params, "Получен результат ", res, "вместо", result)