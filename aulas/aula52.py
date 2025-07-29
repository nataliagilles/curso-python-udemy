velocidade= 52
local_carro=90

RADAR1= 60
LOCAL_1= 100
RADAR_RANGE=1

velocidade_radar1_de_passou= velocidade > RADAR1
carro_multado_em_radar1= local_carro>=( LOCAL_1 - RADAR_RANGE) and \
    local_carro<= (LOCAL_1 + RADAR_RANGE)

if velocidade_radar1_de_passou:
    print("Carro passou da velocidade")
if carro_multado_em_radar1 and\
        velocidade_radar1_de_passou:
    print("Você foi multado em radar 1")
