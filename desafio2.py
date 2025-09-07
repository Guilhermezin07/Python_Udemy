# O decisor de números:

numero = int(input("digite um numero inteiro para descobrir se par ou impar: "))

if numero % 2 == 0:
    print(f"o numero {numero} é par.")
elif numero % 2 != 0:
    print(f"o numero {numero} é impar.")

numero2 = int(input("digite o numero para ver se é positivo ou negativo: "))

if numero2 >= 0:
    print("o numero é positivo")
elif numero2< 0:
    print("o numero é negativo")