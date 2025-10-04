import matplotlib.pyplot as plt
texto = 'iqzn hdiq l omrn ovncn jle l bianbk dcmqznee. who evn vlf lq nqzvlqornqo hdiq vnc ip l pnlcphb eico jvmzv zihbf iqbk wn wciunq wk bian.'
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
histograma = {}
for letra in alfabeto:
    histograma[letra] = 0
for letra in texto:
    if letra in alfabeto:
        histograma[letra] += 1
print(histograma)
plt.bar(histograma.keys(), histograma.values())
plt.show()