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

nome = "Izabelly"
print(f"Meu nome é: {nome}")

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


