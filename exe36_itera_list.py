# Lista de listas e seus indices 

salas = [

    ['maria', 'helena', ],

    ['elaine',], 

    ['luiz', 'joao', 'eduarda', (10, 20, 30) ]

]

print(salas[2][3][1])

for lista in salas:
    print(f'sala composta por: {lista}')
    for item in lista:
        print(item)
      
       