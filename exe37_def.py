#uma função chamada area que receba dimensoes de um terreno 
#(largura e comprimento) e depois mostre a area do terreno

def area(largura, comprimento):
    a = (largura * comprimento)
    print(f"a area de um terreno de {largura}m por {comprimento}m é de {a}m2")

print("---CONTROLE DE TERRENOS----")
l = int(input("digite largura: "))
c = int(input("digite o comprimento: "))
area(l,c)
