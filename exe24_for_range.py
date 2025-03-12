texto = 'nome-de-+' # iteravel
iterator = iter(texto) # iterator 

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break

# codigo acima reflete como funciona o for debaixos dos panos :
# e o codigo abaixo reflete a real utilizacao do for:

for letra in texto:
    print(letra)