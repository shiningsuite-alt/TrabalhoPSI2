def fatorial_idade(n):
    if n==1:
        return 1
    else:
       return n * fatorial_idade(n-1)

def calcularimc(x,y):
    imc=float(x)/float(y*y)
    return imc

nome=input("Digite seu nome: ")
morada=input("Digite seu Morada: ")
idade=int(input("Digite sua idade: "))
altura=float(input("Digite sua altura em metros: "))
peso=float(input("Digite seu peso: "))

mensagem="I know where you live "+nome+", "+morada+", you are "+str(idade)+" years old and "+str(altura)+" metres tall, i will get you."
print(mensagem)

print("Here is the factorial number of your age:")
fatorial=fatorial_idade(idade)
print(int(fatorial))

print("Here is your IMC:")
IMC=calcularimc(peso,altura)
print(float(IMC))
if IMC<18:
    print("ganhar algum peso")
elif 18 <= IMC <= 25:
    print("peso normal")
elif 25 < IMC <= 30:
    print("perder algum peso")
elif IMC>30:
    print("Gordo")
