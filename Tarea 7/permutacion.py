import itertools
mascotas = ['perros', 'pajaros', 'gatos', 'peces']
combo_mas = list(itertools.permutations(mascotas))
for mas_tail in combo_mas:
    mas = mas_tail[:1] + ('caballos',) + mas_tail[1:]
    print(mas)# Fijar caballos en la casa del medio