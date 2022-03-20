import math
from urllib.request import DataHandler
dados=[32.3,62.2,10.3,22.0,13.1,9.9,11.9,20.0,36.4,23.5,18.0,22.6,20.3,38.3,19.6,27.2,28.9,18.4,27.3,21.7,23.7,13.9,36.3,32.9,
29.7,25.4,23.8,15.7,17.0,39.2,22.7,29.9,18.3,33.0]
rol=len(dados)
dados_organizados=[]
print("dados brutos: ",dados)
dados_organizados=dados
dados_organizados.sort()

print("dados organizados: ",dados_organizados)
print(len(dados))
c=0
l_sup=0
l_inf=0
pontoMedio=0
amplitude=0
l_inf=dados[c]
while c != rol:
    if l_inf >= dados[c]:
        l_inf=dados[c]
    if l_sup<=dados[c]:
        l_sup=dados[c]
    c+=1
#numero de classes
nclasses=0
logaritmo=math.log10(rol)
if rol<=25:
    nclasses=5
elif rol >25:
    nclasses=math.ceil(logaritmo*3.22+1)
range=l_sup-l_inf
amplitude=range/nclasses
amplitude=math.ceil(range/nclasses)
pontoMedio=(l_sup+l_inf)/2
print("limite superior: ",l_sup," limite inferior: ",l_inf)
print("range: ",range)
print("amplitude: ",amplitude)
escrever=""

print("numero de classes: ",nclasses)
with open('Probabilidade/resultado.txt','w') as f:
    f.write("Dados: "+ str(dados)+"\n")
    
    f.write("Dados organizados: "+str(dados_organizados)+"\n")
    f.write("Numero Elementos: "+str(rol)+"\n")
    f.write("Range: "+str(range)+"\n")
    f.write("Limite Superior: "+str(l_sup)+"\n")
    f.write("Limite Inferior: "+str(l_inf)+"\n")
    f.write("Numero de Classes: "+str(nclasses)+"\n")
    f.write("Amplitude: "+str(amplitude)+"\n")
    f.close

classe=[]
final=[]
c=0

posicao=0
lista_classes=[]
lista_frequencia=[]
inicio=dados_organizados[0]
final=inicio+amplitude
posicao=0
while c!=nclasses:
    a=posicao
    frequencia=0
    lista_classes.append("["+str(inicio)+","+str(final)+"[")
    while a!=rol:
        if (dados_organizados[a] >= inicio) and (dados_organizados[a]<final):
            frequencia+=1
        a+=1
    posicao+=frequencia
    lista_frequencia.append(str(frequencia))
    inicio=final
    final=final+amplitude

    c+=1
print("lista classes: ",lista_classes)
print("frequencias: ",lista_frequencia)