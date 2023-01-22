"""
Faça um programa na linguagem python que receba as seguintes informações de dez pessoas: idade, peso, altura. Calcule e mostre:
a) A media da idade das pessoas;
b) A quantidade de pessoas com peso superior a 90kg e altura inferior a 1,50 metros;
c) A porcentagem de pessoas com idade entre 10 e 30 anos em relação ao numero total de pessoas.
d) Qual a idade da pessoa mais jovem;
e) Qual a altura da pessoa mais alta;
"""
# Programa para calcular informações de dez pessoas

# Declaração das variáveis
idades = []
pesos = []
alturas = []
quantidade_pessoas_90kg_altura_150 = 0
pessoas_10_30 = 0

# Loop para coletar as informações de dez pessoas
for i in range(3):
    idade = int(input("Informe a idade da pessoa " + str(i+1) + ": "))
    idades.append(idade)
    peso = float(input("Informe o peso da pessoa " + str(i+1) + ": "))
    pesos.append(peso)
    altura = float(input("Informe a altura da pessoa " + str(i+1) + ": "))
    alturas.append(altura)

# Cálculo da média de idade
media_idade = sum(idades) / len(idades)
print("A média da idade das pessoas é:", media_idade)

# Cálculo da quantidade de pessoas com peso superior a 90kg e altura inferior a 1,50 metros
for i in range(10):
    if pesos[i] > 90 and alturas[i] < 1.50:
        quantidade_pessoas_90kg_altura_150 += 1
print("A quantidade de pessoas com peso superior a 90kg e altura inferior a 1,50 metros é:", quantidade_pessoas_90kg_altura_150)

# Cálculo da porcentagem de pessoas com idade entre 10 e 30 anos
for i in range(10):
    if 10 <= idades[i] <= 30:
        pessoas_10_30 += 1
porcentagem_pessoas_10_30 = (pessoas_10_30 / len(idades)) * 100
print("A porcentagem de pessoas com idade entre 10 e 30 anos é:", porcentagem_pessoas_10_30, "%")

# Cálculo da idade da pessoa mais jovem
idade_pessoa_mais_jovem = min(idades)
print("A idade da pessoa mais jovem é:", idade_pessoa_mais_jovem)

# Cálculo da altura da pessoa mais alta
altura_pessoa_mais_alta = max(alturas)
print("A altura da pessoa mais alta é:", altura_pessoa_mais_alta)