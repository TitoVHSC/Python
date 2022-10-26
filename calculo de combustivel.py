def calculoviagem(distancia, velocidademedia):
    tempo = distancia/velocidademedia
    return tempo
    
def calculocombustivel(distancia):
    litros_usados = distancia/12
    return litros_usados
    
velocidademedia = (int(input('Digite a velocidade média da viagem: ')))
distancia = (int(input('Digite a distancia do destino: ')))
tempo = calculoviagem(distancia, velocidademedia)
litros_usados = calculocombustivel(distancia)

print(f'   o tempo gasto na viagem foi de {tempo:.1f}h para percorrer uma distancia de {distancia}km em uma velocidade média de {velocidademedia}km/h, consumindo um total de {litros_usados:.2f} litros de combustivel')