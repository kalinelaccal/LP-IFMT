'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q1():
    nome = "Kaline"
    print ('-q1')
    #print(f'{nome}')
    print(nome)


#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    print ('-q2')
    produto = 30*27
    print(produto)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    print ('-q3')
    media = (5+8+12)/3
    print (media)

#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    print ('-q4')
    inteiro = int(input('Digite um número inteiro: '))
    print (inteiro)

#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    print("-q5")
    num1=float(input("digite o primeiro numero: "))
    num2=float(input("digite o segundo numero: "))
    print(f"o primeiro numero é {num1} e o segundo é {num2}")
    

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    print("-q6")
    num1=int(input("digite um número inteiro: "))
    print(f"O número antecessor é {num1-1} e o sussessor é {num1+1}")

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    print("-q7")
    nome=input("Insira seu nome: ")
    endereço=input("Insira seu endereço: ")
    telefone=input("insira seu telefone: ")
    print("Dados inseridos:")
    print(f"Nome: {nome}")
    print(f"Endereço: {endereço}")
    print(f"Telefone: {telefone}")

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    print("-q8")
    num1=int(input("Insira o primeiro número inteiro: "))
    num2= int(input("Insira o segundo número inteiro: "))
    print(f"{num1} menos {num2} é igual a {num1-num2}")

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    num1=float(input("Insira um número real: "))
    print(f"1/4 de {num1} é igual a {num1/4}")


#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1=float(input("Insira o primeiro número: "))
    num2=float(input("Insira o segundo número: "))
    num3=float(input("Insira o terceiro número: "))
    print(f"A média aritmética entre {num1}, {num2} e {num3} é: {(num1+num2+num3)/3}")

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1=float(input("Insira o primeiro número: "))
    num2=float(input("Insira o segundo número: "))
    print(f"{num1} + {num2} = {num1+num2}\n{num1} - {num2} = {num1-num2}\n{num1} * {num2} = {num1*num2}\n{num1} / {num2} = {num1/num2}")

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    num1=float(input("Insira um número real: "))
    print(f"O quadrado de {num1} é igual a: {num1**2}")

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo=float(input("Insira o saldo da poupança: "))
    print(f"O saldo de {saldo} foi atualizado para {saldo+(saldo*2)/100} com o reajuste de 2%.")
    #ou saldo+(saldo*0.02)

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura / 2).

####### Perimetro: (b+a)*2 ######## Area: b*a #########
def q14():
    base=float(input('Insira a base do retângulo: '))
    altura=float(input('Insira a altura do retângulo: '))
    print(f'Perímetro: {(base+altura)*2} \nÁrea: {base*altura}')

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    valor=float(input('Insira o valor do produto: '))
    desconto=float(input('Insira o % de desconto desejado: '))
    print(f'Valor do desconto: {valor*(desconto/100)} \nValor do produto com desconto: {valor-(valor*(desconto/100))}')

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    salario=float(input('Insira o valor do salário atual: '))
    reajuste=float(input('Insira o % de reajuste: '))
    print(f'Valor do salário com reajuste: {salario+(salario*(reajuste/100))}')

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

###### F = (C × 9/5) + 32
def q17():
    c=float(input('Insira o valor em centígrados: ')) 
    print(f'{c}ºC, em Fahrenheit é : {(c*(9/5))+32}ºF')

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
    tempo=float(input('Insira o tempo decorrido na viagem (horas): '))
    velocidade=float(input('Insira a velocidade média (km/h): '))
    distancia=tempo*velocidade
    litros= distancia/12
    print(f'Foram consumidos {litros} litros de conbustível, considerando consumo de 12km/L.')

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
    valor=float(input('Insira o valor da prestação vencida (R$): '))
    taxa=float(input('Insira a taxa periódica de juros (%): '))
    atraso=int(input('Insira o período de atraso (meses): '))
    juros=valor*(taxa/100)*atraso
    print(f'A prestação de R${valor} está vencida a {atraso} meses, somando R${juros}. \nO valor atual é de R${valor+juros}')

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():
    valor=float(input('Insira o valor em Dolar (U$):'))
    cotação=float(input('Insira o valor da cotação do Dolar (R$):'))
    print(f'U${valor} = R${valor*cotação}')
q20()

