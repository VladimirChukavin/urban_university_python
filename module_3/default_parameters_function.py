# Параметры по умолчанию внутри функции

def func(a=2, b=5):
    print(a + b)


func()
func()
func()
func()

func(1, 8)


def test(a, b=3, c=2):
    print(a + b - c)


test(44)


def func_params(a, b=3, c=[]):
    c.append(a + b)
    print(c)


func_params(7)
func_params(7)
func_params(7)
func_params(7)


def func_params_one(a, b=3, c=None):
    if c is None:
        c = [a + b]
    print(c)


func_params_one(1)
func_params_one(2)
func_params_one(3)
func_params_one(4)
