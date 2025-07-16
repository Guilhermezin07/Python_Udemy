#função escreva que receba um texto e mostre uma mensagem junto com 
# uma linha adaptavel ao tamanho da palavra

def escreva(msg):
    print("-" *(len(msg)))
    print(msg)
    print("-" *(len(msg)))
    

mensagem = input("escreva mensagem: ")
escreva(mensagem)
