dic={'SP':67836.43,
'RJ':6678.66,
'MG':29229.88,
'ES':27165.48,
'Outros':19849.53}

soma=0
for i in dic.values():
  soma+=i
lst=list(dic.values())


for i,j in dic.items():
   dic[i] =(j/soma)

for i,j in dic.items():
  
  print(i,j*100,'%')