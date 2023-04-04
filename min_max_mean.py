import json
with open("dados.json") as file:
    data = json.load(file)
    
dias=len(data)
count=0
for i in data:
    if i['valor']==0:
        count+=1

soma=0
for i in data:
    soma+=i['valor']
    
media=soma/(dias-count)

cont_dias=0
for i in data:
    if i['valor']>media:
        cont_dias+=1
        

valmax=0
for i in data:    
        if i['valor']>valmax:
            valmax=i['valor']
            
valmin=1000000
for i in data:    
        if i['valor']<valmin and i['valor']!=0:
            valmin=i['valor']
print('Valor máximo: ',valmax,"Valor mínimo: ",valmin,"Dias acima da média: ",cont_dias)

    