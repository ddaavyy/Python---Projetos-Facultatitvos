"""

Bem-Vindo ao meu código :D


"""

valores = input("Bem-vindo ao removodor de duplicatas.\nDigite os valores que entraram na lista, separados por vírgula: ")
lista = [valor.strip() for valor in valores.split(",")]
lista2 = []

for v in lista:
    if v not in lista2:
        lista2.append(v)

print(f"Sua lista original era:\n{lista}\n\nCom os valores duplicados removidos ela ficou:\n{lista2}")