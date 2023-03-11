lista = [1,2,1,3,3,1,2,1,5,1]
histograma = {1:0,2:0,3:0,4:0,5:0}
for numero in lista:
    histograma[numero] +=1
for numero in sorted(histograma.keys()):
    print(str(numero), ":", "*" * histograma[numero])