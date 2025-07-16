velocidade = int(input("digite a velocidade"))  # velocidade atual do carro
local_carro = int(input('digite o local em km'))   # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega 

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_local_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_local_2 =  local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_passou_radar_1 = carro_local_1 and carro_local_2

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

# objetivo - saber se o carro passou da velocidade do radar
if vel_carro_pass_radar_1:
    print('voce passou do limite do radar 1')

elif carro_passou_radar_1:
    print('carro passou pelo radar 1 e esta dentro do limite')

elif carro_multado_radar_1:
    print('carro foi multado no radar 1')