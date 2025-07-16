velocidade_atual = int(input("Digite a velocidade atual do carro (em km/h): "))
localizacao_carro_km = int(input('Digite a localização atual do carro na estrada (em km): '))

velocidade_maxima_radar1 = 60  # Velocidade máxima permitida no radar 1
localizacao_radar1_km = 100    # Localização do radar 1 na estrada (em km)
alcance_radar_km = 1          # Distância de alcance do radar (em km para cada lado)

excedeu_velocidade_radar1 = velocidade_atual > velocidade_maxima_radar1

limite_inferior_radar1_km = localizacao_radar1_km - alcance_radar_km
limite_superior_radar1_km = localizacao_radar1_km + alcance_radar_km
carro_na_area_radar1 = localizacao_carro_km >= limite_inferior_radar1_km and localizacao_carro_km <= limite_superior_radar1_km

carro_multado_radar1 = excedeu_velocidade_radar1 and carro_na_area_radar1

# objetivo - saber se o carro passou da velocidade do radar
if carro_multado_radar1:
    print('O carro foi multado no radar 1.')
elif carro_na_area_radar1:
    print('O carro passou pelo radar 1 dentro do limite de velocidade.')
elif excedeu_velocidade_radar1:
    print('Atenção! O carro está acima do limite de velocidade.')
else:
    print("o carro esta fora da area do radar")