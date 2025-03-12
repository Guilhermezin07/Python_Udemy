condicao_1 = True 
passou_no_if = None

if condicao_1:
    passou_no_if = True
    print('faca algo')
else:
    print('nao faca nada')

if passou_no_if is None:
    print('nao passou no if')
if passou_no_if is not None:
    print('passou no if')