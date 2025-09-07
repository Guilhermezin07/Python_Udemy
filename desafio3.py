# O mestre das listas:

cidades = ['londres', 'paris', 'roma', 'madrid', 'lisboa']
print(cidades)

while True:
    item = input("digite um nome de uma cidade para adicionar a lista: ")
    

    if item.lower() == 'sair':
        break
   

    cidades.append(item)
    print(f"{item} foi adicionada a lista de cidades")


    print("\nLista Atualizada:", cidades) 
    print("\npara encerrar,  digite 'sair' ")