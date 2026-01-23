password="AH@12#ree"

idade=int(input("Qual a sua idade:"))

if idade>=18:
    print("You are of age")
else:
    print("You are not of age")

nota=int(input("Qual a sua nota:"))

if nota==20:
    print("perfeito")
elif 15 < nota < 20:
    print("excelento")
elif 10<=nota<=15:
    print("Aprovado")
elif 5<nota<10:
    print("Reprovado")
elif 0<=nota<=5:
    print("Burro")
else:
    print("Erro")

tentativas=0
login=False

while tentativas<3 and login==False:
    palavra_passe=input("Escreva o seu palavra-passe para salvar:")
    if palavra_passe==password:
        login=True
        print("login com sucesso")
    else:
        tentativas+=1
        mensagem="Palavra-Passe invalida, tens "+str(3-tentativas)+" tentativas"
        login=False
        print(mensagem)

if login:
    for i in range(10):
        print("Parabens")
if not login:
    for i in range(10):
        print("Dumbass")