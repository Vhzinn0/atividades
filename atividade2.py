altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

imc = peso / (altura ** 2)

print("Seu IMC é: ", round(imc, 2))