nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))


maior_de_idade = idade >= 18


print("Nome completo: " + nome + " " + sobrenome)
print("Idade: " + str(idade))
print("Altura: " + str(altura) + " metros")
print("Peso: " + str(peso) + " quilogramas")
print("Maior de idade: " + str(maior_de_idade))