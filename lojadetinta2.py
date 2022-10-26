areapintada = (float(input('Insira quantos metros quadrados serão pintados: ')))

latadetinta = 108
galao = 21.6
# os numeros acima sao referente a quantos metros quadrados cada uma rende #

latasusadas = areapintada/108
galoesusados = areapintada/21.6

totallata = latasusadas*80
totalgalao = galoesusados*25


print(f'Para pintar uma área de {areapintada} metros quadrados irá utilizar {latasusadas:.2f} latas de tinta e o custo em tinta será de {totallata:.2f} reais, utilizando galões, serão necessários {galoesusados:.2f} galões de tinta e irá custar {totalgalao:.2f} reais ')
