palavra=str(input("Digite a string para ser invertida: "))

lista=list(palavra)
reverse=[]

for i in range(len(lista)):
    reverse.append(lista[len(lista)-i-1])
    
rev=''.join(reverse)   
print(rev)