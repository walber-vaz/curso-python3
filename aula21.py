# variáveis e contantes
# complexidade de código

# variáveis
velocidade = 61
local_carro = 100

# constantes
RADAR = 60
LOCAL = 100
RADAR_RANGE = 1

velocidade_carro = velocidade > RADAR
carro_multado = (
    local_carro >= (LOCAL - RADAR_RANGE)
    and local_carro <= (LOCAL + RADAR_RANGE)
    and velocidade_carro
)

if velocidade_carro:
    print("Você passou no radar!")

if carro_multado:
    print("Carro multado!")
