areapintada = (float(input('Insira quantos metros quadrados serão pintados: ')))
latadetinta = 54
latasusadas = areapintada/54
preçototal = latasusadas*80

print(f'Para pintar uma área de {areapintada} metros quadrados irá utilizar {latasusadas:.2f} latas de tinta e o custo em tinta será de {preçototal:.2f} reais')