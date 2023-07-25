import random
from statistics import mode, mean, median
import pandas #analise de dados, cortar graficos 

arr = []
random.seed(1)

for i in range(200):
    arr.append(random.randint(0,100))

print(arr)

#for i inramge(100)
#print(i, arr,count(i))


#arrModa = arr.copy
#posicoes = []
#removidos = 0


for pos,num in enumerate(arr):
    if num == 70:
        print(pos)

print("Media: ", mean(arr))
print("Mediana: ", median(arr))
print("Menor termo ", min(arr))
print("Menor termo ", max(arr))

arrQ = arr.copy()
arrQ.sort()

df = pandas.DataFrame(arrQ)
quartis = df.quantile([0.25,0.5,0.75,1])
q1 = quartis[0][0.25]
q2 = quartis[0][0.5]
q3 = quartis[0][0.75]
q4 = quartis[0][1]


countQ1 = 0
countQ2 = 0
countQ3 = 0
countQ4 = 0

for i in arrQ:
    if i <= q1:
        countQ1 += 1
    elif i <= q2:
        countQ2 += 1
    elif i <= q3:
        countQ3 += 1
    else: 
        countQ4 += 1
print("Q1: ",q1,"Quantidade:",countQ1)
print("Q2: ",q2,"Quantidade:",countQ2)
print("Q3: ",q3,"Quantidade:",countQ3)
print("Q4: ",q4,"Quantidade:",countQ4)

countLower = 0
countHigher = 0

for i in arrQ:
    if i < 50:
        countLower += 1
    else:
        countHigher += 1
print("Numeros acima de 50 ", countLower)
print("Numeros abaixo de 50 ", countHigher)
