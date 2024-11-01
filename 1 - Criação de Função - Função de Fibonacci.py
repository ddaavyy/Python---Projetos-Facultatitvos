"""

Bem-Vindo ao meu código :D


"""

def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat

def fibonacci(n):
    if n < 0:
        print(f"O número {n} é negativo.")
    f = 0
    num = num2 = 1
    if n == f or n == num:
        return print(f"{n} está na sequencia de Fibonnaci.")
    else:
        while n != num2:
            num2 = f + num
            f = num
            num = num2
            if num2 > n:
                return print(f"{n} NÃO está na sequencia de Fibonnaci.")
            if num2 == n:
                return print(f"{n} ESTÁ na sequencia de Fibonnaci.")

resp = True
while resp == True:
    r = int(input((f"\nMENU:\n1 - Fatorial\n2 - Fibonnaci\nEscolha sua opção: ")))
    if r == 1:
        num = int(input("\nEscolha um número para saber seu fatorial: "))
        print(f"O fatoral de {num} é: {fatorial(num)}\n")
    if r == 2:
        fibonacci(int(input("\nEscolha um número para saber se ele esta presente na sequencia de fibonnaci: ")))
    r = str(input("Deseja voltar ao menu (S / N)? -> "))
    r.lower()
    if r == "n":
        resp = False
