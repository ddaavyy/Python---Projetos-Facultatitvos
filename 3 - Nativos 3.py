"""

Bem-Vindo ao meu código :D


"""

from decimal import Decimal, getcontext

# Definir a precisão dos cálculos
getcontext().prec = 6

def length_conversion(value, from_unit, to_unit):
    """Converter unidades de comprimento."""
    conversions = {
        'metro': 1,
        'kilometro': 0.001,
        'centimentro': 100,
        'milimetro': 1000,
        'milha': 0.000621371,
        'jarda': 1.09361,
        'pe': 3.28084,
        'polegada': 39.3701,
        'metros': 1,
        'kilometros': 0.001,
        'centimentros': 100,
        'milimetros': 1000,
        'milhas': 0.000621371,
        'jardas': 1.09361,
        'pes': 3.28084,
        'polegadas': 39.3701
    }
    return value * Decimal(conversions[from_unit]) / Decimal(conversions[to_unit])

def weight_conversion(value, from_unit, to_unit):
    # Converter unidades de peso.
    conversions = {
        'kilograma': 1,
        'grama': 1000,
        'miligrama': 1_000_000,
        'libra': 2.20462,
        'onça': 35.274,
        'kilogramas': 1,
        'gramas': 1000,
        'miligramas': 1_000_000,
        'libras': 2.20462,
        'onças': 35.274
    }
    return value * Decimal(conversions[from_unit]) / Decimal(conversions[to_unit])

def temperature_conversion(value, from_unit, to_unit):
    # Converter unidades de temperatura.
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius':
        return value * 9 / 5 + 32 if to_unit == 'fahrenheit' else value + 273.15
    if from_unit == 'fahrenheit':
        return (value - 32) * 5 / 9 if to_unit == 'celsius' else (value - 32) * 5 / 9 + 273.15
    if from_unit == 'kelvin':
        return value - 273.15 if to_unit == 'celsius' else (value - 273.15) * 9 / 5 + 32

def main():
    while True:
        print("\nConversor de Unidades")
        print("1. Comprimento")
        print("2. Peso")
        print("3. Temperatura")
        print("4. Sair")
        choice = input("Escolha uma categoria para converter: ")

        if choice == '1':
            value = Decimal(input("Digite o valor: "))
            from_unit = input("De (metro(s), kilometro(s), centimentro(s), milimetro(s), milha(s), jarda(s), pe(s), polegada(s)): ")
            to_unit = input("Para (metro(s), kilometro(s), centimentro(s), milimetro(s), milha(s), jarda(s), pe(s), polegada(s)): ")
            result = length_conversion(value, from_unit, to_unit)
            print(f"{value} {from_unit} é igual a {result} {to_unit}")

        elif choice == '2':
            value = Decimal(input("Digite o valor: "))
            from_unit = input("De (kilograma(s), grama(s), miligrama(s), libra(s), onça(s)): ")
            to_unit = input("Para (kilograma(s), grama(s), miligrama(s), libra(s), onça(s)): ")
            result = weight_conversion(value, from_unit, to_unit)
            print(f"{value} {from_unit} é igual a {result} {to_unit}")

        elif choice == '3':
            value = float(input("Digite o valor: "))
            from_unit = input("De (celsius, fahrenheit, kelvin): ")
            to_unit = input("Para (celsius, fahrenheit, kelvin): ")
            result = temperature_conversion(value, from_unit, to_unit)
            print(f"{value} {from_unit} é igual a {result} {to_unit}")

        elif choice == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

print("Bem-vindo ao meu conversor ATUALIZADO de medidas.")
main()