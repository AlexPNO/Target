
def fibo(n):
  if n==0:
    return 0
  elif (n==1):
    return 1
  
  return fibo(n-1)+fibo(n-2)

n=int(input("Digite um número:"))
lst=[]
for i in range(n+2):
  lst.append(fibo(i))

if n>=16:
  for i in range(n//2):
    lst.append(fibo(i))
  
# print(lst)
print(n in lst)
    

 
    
    

  