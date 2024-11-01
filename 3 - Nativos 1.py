"""

Bem-Vindo ao meu código :D


"""

import random
import calendar


def gerar_data_aleatoria(a, b):
    ano = random.randint(a, b)  # Gera um ano entre 1 a 2100
    mes = random.randint(1, 12)  # Gera um mês entre 1 e 12
    
    
    max_dias = calendar.monthrange(ano, mes)[1] # Obter o número máximo de dias no mês e ano gerado
    dia = random.randint(1, max_dias)  # Gera um dia válido para o mês e ano
    
    return ano, mes, dia


def nome_dia_semana(dia_semana):
    dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    return dias[dia_semana]


def nome_mes_portugues(mes):
    if mes == 1:
        return "Janeiro"
    elif mes == 2:
        return "Fevereiro"
    elif mes == 3:
        return "Março"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Maio"
    elif mes == 6:
        return "Junho"
    elif mes == 7:
        return "Julho"
    elif mes == 8:
        return "Agosto"
    elif mes == 9:
        return "Setembro"
    elif mes == 10:
        return "Outubro"
    elif mes == 11:
        return "Novembro"
    elif mes == 12:
        return "Dezembro"

print("Digite o periodo dos anos que deseja gerar uma data aleatória (de xxxx (sem números negativos) ate xxxx (sem números negativos)).")
resp1 = int(input("De: "))
resp2 = int(input(f"De {resp1} entre: "))

ano, mes, dia = gerar_data_aleatoria(resp1, resp2) # Gerando data

print(f"A data gerada é: {dia} de {nome_mes_portugues(mes)} de {ano}. Esta data cai em uma {nome_dia_semana(calendar.weekday(ano, mes, dia))}")
