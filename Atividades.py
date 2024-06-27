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