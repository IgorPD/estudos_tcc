def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fib(n - 1) + fib(n - 2)


def multiply(n):
    if n == 0:
        #print(f"Multiply({n}) = 0")
        return 0
    elif n == 1:
        print(f"Desempilhando({n}) = 1")
        return 1
    else:
        print(f"Empilhando n = {n}")
        retorno = multiply(n - 1)
        var = retorno * n
        print(f"Desempilhando({n}) = {var}")
        return var


if __name__ == '__main__':
    print(multiply(10))
