#MEU PRIMEIRO PHYTON

print("Olá mundo")
print("Primeiro estamos praticando o comando Print")
print("Esse comando printa 3 linhas de texto")

print("Izabelly")
print("Minha casa")
print(19)

#variavel e constante 'nome' pode ser fixa ou variar
nome = input ("Digite seu nome:")
print("Olá" + nome)

#string f 

resultado = 25 
resultado2 = 30
print(f"oresultado da conta é: {resultado}")
#ou
print("o resultado da conta é:{}".format(resultado))

print(f"o resultado dos dois valores é: {resultado}, e a conta de dois valores é {resultado2}")
print("o resultado dos dois valores é: {}, e a conta de dois valores é {}".format(resultado, resultado2))


#PARA FAZER A CONVERSÃO

# convertToInteiro = int('nome da variavel')
# convertToString = str('nome da variavel')
# convertToFloat = float('nome da variavel')


#pratica 1

ano = int(input("Coloque o ano que vc nasceu aqui: "))
print(f"Ao fim do ano vc terá: {2024 - ano}")

#pratica 2

altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso? "))
imc = peso / (altura / 100) ** 2

print(f"O IMC é: {imc}")

#pratica 3

nome2 = "Izabelly"
print(f"Meu nome é: {nome2}")

#pratica 4

idade= 19
print(f"tenho {idade} anos")

#pratica 5

habilidade1 = "oioioi"
habilidade2 = "oioiooi"
habilidade3 = "oioioi"
skill = "python"
level = "iniciante"

print(f"Minhas habilidades são: {skill} {habilidade1} {level}, {habilidade2} , {habilidade3}" )

#pratica 6

salario= 2000
salario2 = 3000

print(f"Procuro um emprego com um salário de {salario} a {salario2} euros por mês.")


#TESTE IF ELSE

#teste 1
idade2 = 18
if idade2 >= 18:
   print("Você é maior de idade")

#teste 2

numero = int(input("Entre com um número: "))

if numero <0:
    print("Esse número é negativo")

if numero >0:
    print("Esse número é positivo")

if numero ==0:
    print("Esse numero é 0")

# TESTE ELIF

gol_casa = int(input("Pontuação de casa: "))
gol_fora = int(input("Pontuação de fora: "))

if gol_casa > gol_fora:
    print("O tie de casa é capeão!")
elif gol_fora > gol_casa:
    print("O time de fora é campeão!")

else:
    print("Empate!")

# TESTE AND (E)

numero2 = int(input("Entre com um número: "))

if numero2 >= 5 and numero2 <= 8:
    print("O numero esta entre 5 e 8")

# TESTE OR (OU)

numero3 = int(input("Entre com um número: "))

if numero3 < 5 or numero3 > 8:
    print("O número esta entre 5 e 8")

numero4 = int(input("Entre com um número: "))

if not (numero4 < 5 or numero4 > 8): # a condição é verdadeira, com o NOT se torna falsa
    print("O número esta entre 5 e 8")

# TESTE WHILE (LOOPING DE REPETIÇÃO)

while True:
    numero5 = int(input("Entre com um número ou digite -1 para parar: "))

    if numero5 == -1:
        break
    print(numero5 ** 2)

print("Programa encerrado, obrigado!")

# TESTE WHILE 2

while True:
    codigo = input("Por favor, insira o PIN: ")

    if codigo == "1234":
        break
    print("Errado!... Tente de novo.")

print("PIN correto! Obrigado")

# 

numero7 = 5
print("Contando")

while True:
    print(numero7)
    numero7 = numero7 - 1
    if numero7 > 0:
        break
    print("Fall")

#

tentativas = 0 # total de tentativas
while True:
    codigo2 = input("Por favor, digite seu PIN: ")
    tentativas += 1 # a cada tentativa será inserido +1 nas tentativas

    if codigo2 == "1234": #se o PIN inserido for este, o print estará correto e mostrará o segundo print
        sucesso = True  # se o pin não estiver correto, aumentará o número das tentativas com o primeiro print
        break

    if tentativas == 3: # quando as tentativas chegarem ao número 3 aparecerá o terceiro print
        sucesso = False
        break

    print("incorreto...tente novamente")
if sucesso:
    print("PIN correto inserido")
else:
    print("Muitas tetativas...")

# TESTE LOOP COM CONDIÇAÕ

numero6 = int(input("Insira um número: "))

while numero6 < 10: # enquanto o numero for menor que dez, printará o resultado da variável
    print(numero6)
    numero6 += 1

print("Execução finalizada")

# EXPRESSÕES REGULARES (BIBLIOTECA)

import re

print(re.search("[A-Z]", "Senha")) #procurará na bibioteca a letra maiúscula na palavra 'Senha'
print(re.search("[a-z]", "Senha")) #procurará na bibioteca as letras minúscula na palavra 'Senha'
print(re.search("[0-9]", "Senha")) #procurará na bibioteca números de 0 a 9 na palavra 'Senha'

# BIBLIOTECA DE NÚMERO RANDÔMICOS

import random

numero_secreto = random.randint(1,100) #será printado um número aleatório de 1 a 100

print(numero_secreto)

# WHILE COM STRING
#irá concatenar as variaveis e printará os resultado
inicio = "ex"
fim = "emplo"
palavra2 = inicio + fim
print(palavra2)

# repetirá a palavra 3 vezes
palavra = "banana"
print(palavra * 3)

#

string_entrada = input("Digite uma string: ")
print(string_entrada) #imprime a string
print("-" * len(string_entrada)) #imprime uma linha de traços com o mesmo comprimento da string digitada

#

string_entrada2 = input("Digite uma string: ")

print(string_entrada2[0])
print(string_entrada2[2])
print(string_entrada2[3])

print("Ultimo caracter" , string_entrada2[len(string_entrada2)] - 1)
