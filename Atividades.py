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