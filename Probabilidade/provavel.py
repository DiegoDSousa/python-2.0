import math
from urllib.request import DataHandler
dados=[230,235,200,175,170,290,181,245,150,190,120,145,220,225,215,195,200,230,
240,200,230,165,265,210,250,210,215,190,270,250]
rol=len(dados)
dados_organizados=[]
dados_organizados=dados

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

escrever=""
print("dados brutos: ",dados)



with open('resultado.txt','w') as f:
    f.write("Dados: "+ str(dados)+"\n")
    dados_organizados.sort()
    f.write("Dados organizados: "+str(dados_organizados)+"\n")
    f.write("Numero Elementos: "+str(rol)+"\n")
    f.write("Range: "+str(range)+"\n")
    f.write("Limite Superior: "+str(l_sup)+"\n")
    f.write("Limite Inferior: "+str(l_inf)+"\n")
    f.write("Numero de Classes: "+str(nclasses)+"\n")
    f.write("Amplitude: "+str(amplitude)+"\n")
    f.close

print("dados organizados: ",dados_organizados)






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





#prints no terminal

print("limite superior: ",l_sup," limite inferior: ",l_inf)
print("range: ",range)
print("numero de classes: ",nclasses)
print("amplitude: ",amplitude)

print("lista classes: ",lista_classes)
print("frequencias: ",lista_frequencia)