def multi(*args):
    result = 1
    for i in args:
        result *= i
    return result


resultado = multi(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(resultado)


def is_par_or_impar(num: int) -> str:
    if num % 2 == 0:
        return f"{num} é par"
    else:
        return f"{num} é impar"


return_list = is_par_or_impar(1)
print(return_list)
