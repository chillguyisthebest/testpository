"""""def uppercase_result(old_func):
    def new_func(*args, **kwargs):
        res = old_func(*args, **kwargs)
        if isinstance(res, str):
            return res.upper()
        return res
    return new_func"""


"""def check_division(old_func):
        def new_func(a, b):
            if b == 0:
                  return("Деление на ноль невозможно")
            return old_func(a, b)
        return new_func """


"""try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print('Вводите только числа!')
except ZeroDivisionError:
    print('Делить на 0 нельзя')
except Exception:
    print('Ошибка. Вам очень "повезло":)')
finally:
    print('Хорошего дня!')"""


def save_result(old_func):
    def new_func(*args, **kwargs):
        res = old_func(*args, **kwargs)
        with open('Calc.txt', 'a', encoding='utf=8') as f:
            f.write(f'{res}\n')
            return res
    return new_func