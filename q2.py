text = input("digite uma string: \n")
cont=0
for i in text:
  if(i == 'a' or i == 'A'):
    cont+=1
print("a letra a/A aparece " + str(cont) + " vezes.")
