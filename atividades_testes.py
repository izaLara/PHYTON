# #atividade 20
#  #será solicitado dois numeros e uma operação para ocorrer entre eles
# op1 = "*"
# op2 = "+"
# op3 = "-"

# solicitacao = int(input("Escreva um número: "))
# solicitacao2 = int(input("Escreva outro número: "))
# escolha_operacao = input("Escolha um operação: ")

# if escolha_operacao == op1:
#  print(solicitacao * solicitacao2 )

# if escolha_operacao == op2:
#  print(solicitacao + solicitacao2 )

# if escolha_operacao == op3:
#  print(solicitacao - solicitacao2 )

#  #atividade 21

# graus = float(input("Escolha uma temperatura: "))
# conversao = ( graus - 32) /1.8

# if conversao> 0:
#   print(f"{conversao:.2f}° celsius")

# if conversao < 0:
#    print("Brr! Esta frio aqui!")

#atividade 22

# salario_por_hora = float(input("Digite seu salário por hora: "))
# dia = (input("Escolha um dia da semana: "))
# horas = float(input("Quantas horas trabalhadas? "))

# salario = salario_por_hora * horas
# final_de_semana = "Domingo"

# if dia == final_de_semana:
#  print( "Este é seu salário trabalhado no mês (incluindo final de semana): ", salario * 2)
#  print("Este é o seu salário trabalado em dias da semana: ", salario)

 #atividade 23

#  pontos = input("Digite a quantidade de pontos no cartão:")

#  if pontos < 100: #Se a taxa for menor que 100 será cobrada uma taxa de 0.10 centavos
#    taxaBonus = 0.10
#  if pontos > 100: #Se a taxa for maior que 100 será cobrada uma taxa de 0.15 centavos
#    taxaBonus = 0.15
 
#  Bonus = pontos * taxaBonus #Multiplicando a quantidade de pontos pela taxa a ser cobrada
#  print(f"O bonus é de : {Bonus:.2f} pontos")

#  #atividade 24

#  previsao = int(input("Previsão do tempo: "))

#  temperatura_f = 0

#  frio = "frio"
#  calor = "calor"

# if previsao == frio:
#  print("Não esqueça de pegar um agasalho antes de sair de casa, pois a temperatura vai cair!")

# if previsao == calor:
#  print("O sol estará radinante hoje! Não esqueça da sua roupa de praia!")

# if previsao == 

#atividade 25

# nota1 = int(input("insira uma nota: "))
# nota2 = int(input("Insira uma nota: "))
# nota_minima = 7

# media = nota1 + nota2 / 2

# if media > nota_minima:
#   print("Aprovado")
# else:
#   print("Reprovado")

 #atividade 26

# idade5 = int(input("Qual a sua idade? "))
# if idade5 > 18:
#   print("Você é de maior")
# else:
#   print("Você é de menor")

 #atividade 27

# gasto = int(input("Insira o valor gasto: "))

# if gasto < 50: # se o valor gasto for menor que 50, imprimira o resultado
#   print("Classe econõmica")

# if gasto > 50 and gasto < 100: # se o valor gasto for maior que 50 e menor que 100, imprimira o resultado
#   print("Classe intermediária")
# else:
#   print("Classe executiva")

# # atividade 28

# idade = int(input("Insira sua idade: "))
# idade_minima = 16
# if idade > idade_minima:
#   print("Pode votar")
# else:
#   print("Não pode votar")

# atividade 30

# numero3 = int(input("Escreva um número: "))
# numero4 = int(input("Escreva outro número: "))

# if numero3 > numero4:
#  print("Este é o maior numero: " , numero3)

# else:
#   print("Este é o maior número: ", numero4)

#atividade 31

# nome6 = input("Escreva seu nome: ")
# idade2 = input("Insira sua idade: ")
# nome7 = input("Escreva seu nome: ")
# idade3 = input("Insira sua idade: ")

# if idade2 > idade3:
#   print("Este é o(a) idoso(a): " ,nome6)
# elif idade3 > idade2:
#   print("Este é o(a) idoso(a): " ,nome7)
# else:
#   print("Elas tem a mesma idade")

#atividade 33

# idade4 = int(input("Qual sua idade? "))

# if idade4 > 0 or idade4 < 5:
#  print("Suspeito que você ainda não saiba escrever")

# elif idade4 > 5 or idade4 > 100:
#  print("Ok, você tem", idade4, " anos.")

#atividade 34 

# nome8 = input("Insira seu nome: ")
# sobrinhos_pato_donald1 = "Huguinho"
# sobrinhos_pato_donald2 = "Zezinho"
# sobrinhos_pato_donald3 = "Luizinho"

# sobrinhos_mickey_mouse1 = "Chiquinho"
# sobrinhos_mickey_mouse2 = "Francisquinho"

# if nome8 == sobrinhos_pato_donald1 or nome8 == sobrinhos_pato_donald2 or nome8 == sobrinhos_pato_donald3:
#   print("Você é um dos sobrinhos do Pato Donald!")

# elif nome8 == sobrinhos_mickey_mouse1 or nome8 == sobrinhos_mickey_mouse2:
#   print("Você é um dos sobrinhos do Mickey Mouse!")

# else:
#   print("Legal!")

#Atividade 35

# ponto_dos_cursos = int(input("Insira seus pontos: "))

# if ponto_dos_cursos < 0:
#   print("Impossível")

# elif ponto_dos_cursos > 0 and ponto_dos_cursos < 49:
#   print("Falhar")

# elif ponto_dos_cursos > 50 and ponto_dos_cursos < 59:
#   print("Sua nota é: 1")

# elif ponto_dos_cursos > 60 and ponto_dos_cursos < 69:
#   print("Sua nota é: 2")

# elif ponto_dos_cursos > 70 and ponto_dos_cursos < 79:
#   print("Sua nota é: 3")

# elif ponto_dos_cursos > 80 and ponto_dos_cursos < 89:
#   print("Sua nota é: 4")

# elif ponto_dos_cursos > 90 and ponto_dos_cursos < 99:
#   print("Sua nota é: 5")

# else:
#   print("Impossível")

#atividade 36

#incompleto

# numero5 = int(input("Insira um número: "))

# if numero5:
#   print("Fizz")
# elif numero5:
#   print("Buzz")
# elif numero5 and numero5:
#   print("FizzBuzz.")
# else:
#   print("Este número não é divisível nem por 3 nem por 5")

#atividade 37

#incompleto
# ano3 = int(input("Insira um ano: "))
# ano4 = 366

# if ano3 / 4:
#   print("Esse é um ano bissexto")

# else:
#   print("Este ano não é bissexto")

#--------------

ano3 = int(input("Insira um ano: "))

if ano3 / 4 and ano3 / 100 and 400:
  print("Esse é um ano bissexto")

else:
  print("Este ano não é bissexto")