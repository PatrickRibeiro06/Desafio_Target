def fib(n):
    fib1 = 0
    fib2 = 1
    soma = 0
    while soma < n:
        soma += fib1 + fib2
        fib1 = fib2
        fib2 = soma
    return soma == n

n = int(input("Digite um número: "))

print(fib(n))