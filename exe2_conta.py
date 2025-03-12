#Ordem de precedencia, mesmo calculo 
# com resultados diferentes

conta_1 = 1 + 1 ** 5 + 5 # 7
conta_2 = (1 + 1) ** (5 + 5) # -> 1024
conta_3 = (1 + (0.5 + 0.5)) ** 5 + 5 # -> 37

print(conta_1)
print(conta_2)
print(conta_3)