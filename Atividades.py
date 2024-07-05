 #atividade 1

nome= input("Digite seu nome: ")
endereco= input("Digite seu endereço: ")
apelido = input("Qual seu apelido?")
cidade_codigo_postal = "Curitiba, 83225456"
print("{}{} mora na rua {}, cidade {}".format(nome,apelido, endereco, cidade_codigo_postal ))

 #atividade 2

nome2= input("Digite seu nome: ")
ano = input("Escolha um ano: ")
#conforme é mudado o nome e ano, o texto será alterado
print("{} é uma valente cavaleira, nascida no ano de {}. Certa manhã, {} acordou com um barulho terrível: um dragão se paroximava da aldeia. Somente {} poderia salvar os moradores da aldeia.".format(nome,ano, nome, nome))

 #atividade 3 

cidade = "São Paulo"
print(cidade)
cidade = "Rio de Janeiro"
print(cidade)

 #atividade 4

string = "oio"
inteiro = 254
float = 20.5
print("este é uma string {}, este um inteiro {} e este uma variavel float {}".format(string, inteiro, float))

 #atividade 5

pt1 = "encontrei um parale"
pt2 = "lepipedo"
print((pt1+pt2))

 #atividade 6

#solicita um numero e o resultado mostra ele multiplicado por 5
numero = int(input("Digite um número: "))
resultado = numero * 5
print(f"Seu numero multiplicado por 5 é: {resultado}")

 #atividade 7

#pergunta o nome e ano em que nasceu, em seguida apresenta o texto em print
nome3 = input("Qual seu nome? ")
ano2 =int(input("Em que ano você nasceu? "))
print(f"Olá {nome3}, você fará {2024 - ano2} anos no final de 2024")

 #atividade 8

#Solicita um preço e o percentual de descoto de um produto ao usuario. Calcule o valor, e o resultado será o preço final do produto.
preco = float(input("Digite o preço do produto: "))
desconto = int(input("Qual a porcentagem do desconto? "))
precoDesconto = preco*desconto
ValorFinal = precoDesconto / 100
print(f"O valor final do produto é: {ValorFinal}")


 #atividade 10

Preco2 = float(input("Qual o preço do seu produto? "))
Porcentagem1 = float(input("digite a porcentagem do produto: "))

desconto = preco * Porcentagem1 / 100

print("O preço do produto é {} e o preço final com o desconto é de: {}".format(desconto, Preco2 + desconto))


 #atividade 16

#solicitando um numero inteiro e multiplicando por -1 se ele for menor que 0
num = int(input("Escreva um número: "))
if num<0:
    calculo = num*-1
    print(calculo)

 #atividade 17

nome4 = input("Digite seu nome: ") #solicitando um nome
porcao = int(input("Solicite uma quantidade de porções: ")) #solicitando uma porção
preco_porcao = 5.90 #preço da porção
if nome4 != "Jerry": #se o nome for diferente de jerry
    print(preco_porcao * porcao) #o resultado será a multiplicação das duas variáveis
 
 #atividade 18

numero2 = int(input("Digite um número: "))
if numero2 < 1000:
 print("Este número é menor que 1000")
if numero2 > 1000:
 print("Obrigado!")    
if numero2 < 10  < 100  <1000:
 print("Este número é menor que 1000, menor que 100 e menor que 10")

 #atividade 19

insira_nome = input("Insira seu nome: ")
nome5 = "izabelly"
cidade2 = "Curitiba"
estado = "Paraná"
cep = 123456789

if insira_nome == nome5:
 print(cidade2 , estado , cep)
if insira_nome != nome5:
 print("Esse usuario não existe em nossas bases de dados")

 #atividade 20
 #será solicitado dois numeros e uma operação para ocorrer entre eles
op1 = "*"
op2 = "+"
op3 = "-"

solicitacao = int(input("Escreva um número: "))
solicitacao2 = int(input("Escreva outro número: "))
escolha_operacao = input("Escolha um operação: ")

if escolha_operacao == op1:
 print(solicitacao * solicitacao2 )

if escolha_operacao == op2:
 print(solicitacao + solicitacao2 )

if escolha_operacao == op3:
 print(solicitacao - solicitacao2 )

 #atividade 21 - incompleta

graus = float(input("Escolha uma temperatura: "))
conversao = ( graus - 32) /1.8

if conversao> 0:
  print(f"{conversao:.2f}° celsius")

if conversao < 0:
   print("Brr! Esta frio aqui!")

 #atividade 22

salario_por_hora = float(input("Digite seu salário por hora: "))
dia = (input("Escolha um dia da semana: "))
horas = float(input("Quantas horas trabalhadas? "))

salario = salario_por_hora * horas
final_de_semana = "Domingo"

if dia == final_de_semana:
 print( "Este é seu salário trabalhado no mês (incluindo final de semana): ", salario * 2)
 print("Este é o seu salário trabalado em dias da semana: ", salario)

 #atividade 23

 pontos = input("Digite a quantidade de pontos no cartão:")

 if pontos < 100: #Se a taxa for menor que 100 será cobrada uma taxa de 0.10 centavos
   taxaBonus = 0.10
 if pontos > 100: #Se a taxa for maior que 100 será cobrada uma taxa de 0.15 centavos
   taxaBonus = 0.15
 
 Bonus = pontos * taxaBonus #Multiplicando a quantidade de pontos pela taxa a ser cobrada
 print(f"O bonus é de : {Bonus:.2f} pontos")

 #atividadde 24

 #atividade 25

nota1 = int(input("insira uma nota: "))
nota2 = int(input("Insira uma nota: "))
nota_minima = 7

media = nota1 + nota2 / 2

if media > nota_minima:
  print("Aprovado")
else:
  print("Reprovado")

 #atividade 26

idade5 = int(input("Qual a sua idade? "))
if idade5 > 18:
  print("Você é de maior")
else:
  print("Você é de menor")

 #atividade 27

gasto = int(input("Insira o valor gasto: "))

if gasto < 50: # se o valor gasto for menor que 50, imprimira o resultado
  print("Classe econõmica")

if gasto > 50 and gasto < 100: # se o valor gasto for maior que 50 e menor que 100, imprimira o resultado
  print("Classe intermediária")
else:
  print("Classe executiva")

#atividade 28

idade = input("Insira sua idade: ")
idade_minima = 16

if idade > idade_minima: #se for maior que a idade minima, exibirá o resultado
  print("Pode votar")

else:  #se for menor que a idade minima, exibirá o resultado
  print("Não pode votar")

#atividade 29


# atividade 30
#Encontrar o maior número e exibir o resltado

numero3 = int(input("Escreva um número: "))
numero4 = int(input("Escreva outro número: "))

if numero3 > numero4:
 print("Este é o maior numero: " , numero3)

else:
  print("Este é o maior número: ", numero4)

# atividade 31

#Dois nomes e duas idades, será imprimido o nome de quem for mais velho
nome6 = input("Escreva seu nome: ")
idade2 = input("Insira sua idade: ")
nome7 = input("Escreva seu nome: ")
idade3 = input("Insira sua idade: ")

if idade2 > idade3:
  print("Este é o(a) idoso(a): " ,nome6)
elif idade3 > idade2:
  print("Este é o(a) idoso(a): " ,nome7)
else:
  print("Elas tem a mesma idade")

#atividade 33

idade4 = int(input("Qual sua idade? "))

if idade4 > 0 or idade4 < 5:
 print("Suspeito que você ainda não saiba escrever")

elif idade4 > 5 or idade4 > 100:
 print("Ok, você tem", idade4, " anos.")

#atividade 34

nome8 = input("Insira seu nome: ")
sobrinhos_pato_donald1 = "Huguinho"
sobrinhos_pato_donald2 = "Zezinho"
sobrinhos_pato_donald3 = "Luizinho"

sobrinhos_mickey_mouse1 = "Chiquinho"
sobrinhos_mickey_mouse2 = "Francisquinho"

if nome8 == sobrinhos_pato_donald1 or nome8 == sobrinhos_pato_donald2 or nome8 == sobrinhos_pato_donald3:
  print("Você é um dos sobrinhos do Pato Donald!")

elif nome8 == sobrinhos_mickey_mouse1 or nome8 == sobrinhos_mickey_mouse2:
  print("Você é um dos sobrinhos do Mickey Mouse!")

else:
  print("Legal!")

#Atividade 35

ponto_dos_cursos = input("Insira seus pontos: ")

if ponto_dos_cursos < 0:
  print("Impossível")

elif ponto_dos_cursos > 0 or ponto_dos_cursos < 49:
  print("Falhar")

elif ponto_dos_cursos > 50 or ponto_dos_cursos < 59:
  print("Sua nota é: 1")

elif ponto_dos_cursos > 60 or ponto_dos_cursos < 69:
  print("Sua nota é: 2")

elif ponto_dos_cursos > 70 or ponto_dos_cursos < 79:
  print("Sua nota é: 3")

elif ponto_dos_cursos > 80 or ponto_dos_cursos < 89:
  print("Sua nota é: 4")

elif ponto_dos_cursos > 90 or ponto_dos_cursos < 99:
  print("Sua nota é: 5")

else:
  print("Impossível")

#atividade 36
#incompleta
numero5 = int(input("Insira um número: "))

if numero5:
  print("Fizz")
elif numero5:
  print("Buzz")
elif numero5 and numero5:
  print("FizzBuzz.")

#atividade 37
#incompleta
ano3 = int(input("Insira um ano: "))

if ano3  or ano3  and 400:
  print("Esse é um ano bissexto")

else:
  print("Este ano não é bissexto")


#atividade 38

while True:
    cumprimento = input("Olá, Você quer continuar? ")

    if cumprimento == "não":
        break

print("Okay, até a proxima")


#atividade 39
#incompleta
from math import sqrt
while True:
  numero6 = int(input("Insira um número"))

  if numero6 < 0:
    break
  print("Número inválido")

  if numero6 > 0:
    break
  print(sqrt(numero6))

print("Fim")

#atividade 40

numero7 = 5
print("Contagem regressiva") #contando a partir do 5

while True: 
 print(numero7)
 numero7 = numero7 - 1 # enquanto for verdadeiro imprimira a variavel - 1

 if numero7 == 0: # entrara em looping até ser igual a zero
  break
 
print("Agora!")


#atividade 41

#Digite a senha, se a confirmação for diferente da primeira inserção, repetirá o looping

while True:
 senha = int(input("Digite uma senha: "))
 senha2 = int(input("Confirme a senha: "))
 if senha == senha2:
  break
print(int(input("Digite novamente: ")))

print("Senha correta")
    
#ativiade 42

tentativas = 0 # total de tentativas
while True:
   codigo2 = input("Por favor, digite seu PIN: ")
   tentativas += 1 # a cada tentativa será inserido +1 nas tentativas

   if codigo2 == "4321": #se o PIN inserido for este, o print estará correto e mostrará o segundo print
       sucesso = True  # se o pin não estiver correto, aumentará o número das tentativas com o segundo print
       break

   print("incorreto...tente novamente")
if sucesso:
    print(tentativas)
else:
    print("Muitas tentativas...")

#atividade 45

numero9 = int(input("Digite um número: "))
print("Você está pronto?")

while numero9 >= 0:
 print(numero9)
print("Agora!")

#atividade 47

numero11 = int(input("Digite um número: "))
numero_inicial = 1

#enquanto o numero inicial for menor ou igual ao número digitado, será printado o número inicial multiplicado por 2
while numero_inicial <= numero11: 
  print(numero_inicial)
  numero_inicial *= 2


#atividade 50

#será solicitado uma senha até que a soma de todos os números seja menor ou igual a 100.
soma = 0

while soma <= 100: 
 numeros = int(input("Digite uma série de números: ")) 
 soma += numeros

 print("A soma será: ", soma)

 #atividade 54
while True:
 palavra = str(input("Escreva uma palavra: "))
 palavra2 = str(input("Escreva outra palavra: "))

 if palavra != palavra2:
  print("Digite outra palavra: ")

 if palavra == palavra2:
   break
 
 #atividade PRATICA

 string = input("Digite uma string: ")
 string2 = input("Digite outra string: ")

 if len(string2) < len(string2) or len(string2) > len(string):
   print("As strings não são igualmente longas")
   