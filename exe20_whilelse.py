string = "valor"

i= 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1

else:
    print('o else n tem espaco')
print(" fora do while ")