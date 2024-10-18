from datetime import date, datetime
hoje = datetime.now()

#importar biblioteca para traduzir:
from deep_translator import GoogleTranslator # pip3 install deep-translator

HOJE = datetime.now()
tradutor = GoogleTranslator(source = 'en', target = 'pt')


#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    num1=int(input("Digite um numero inteiro: "))
    num2=int(input("Digite outro numero inteiro: "))
    adc=(num1+num2)
    if(adc > 10):
        print(f'{adc} é maior que 10.')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
    num1=int(input("Digite um numero inteiro: "))
    num2=int(input("Digite outro numero inteiro: "))
    adc=(num1+num2)
    if(adc > 20):
        print(f'{adc} + 8 = {adc+8}')
    elif(adc <= 20):
        print(f'{adc} - 5 = {adc-5}')

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    num=int(input('Insira um número: '))
    if ((num%3)==0):
        print(f'{num} é múltiplo de 3.')
    else:
        print(f'{num} não é múltiplo de 3.')

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
    num=int(input('Insira um número: '))
    if ((num%5)==0):
        print(f'{num} é divisível por 5.')
    else:
        print(f'{num} não é divisível por 5.')

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
    num = int(input('Insira um número: '))
    if ((num%3)==0) and ((num%7)==0):
        print(f'{num} é divisível por 3 e 7.')
    elif ((num%3)==0) and ((num%7)!=0):
        print(f'{num} é divisível por 3 mas não por 7.')
    elif ((num%3)!=0) and ((num%7)==0):
        print(f'{num} é divisível por 7 mas não por 3.')
    elif ((num%3)!=0) and ((num%7)!=0):
        print(f'{num} não é divisível por 3 nem por 7.')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q6():
    salario = round(float(input("Insira o salário bruto: R$")),2)
    prestaçao = round(float(input('Insira o valor da prestação: R$')),2)
    percent = (prestaçao*100)/salario
    if (percent > 30):
        print(f'Valor superior a 30% do salario bruto. O impréstimo não pode ser concedido.')
    else:
        print('Impréstimo autorizado.')    

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7():
    num = int(input('Insira um número: '))
    if (20 <= num <= 50):
        print(f'{num} está entre 20 e 50.')
    else:
        print(f'{num} não está entre 20 e 50.')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
    num = int(input('Insira um número: '))
    if (num < 20):
        print(f'{num} é menor que 20.')
    elif (num == 20):
        print(f'{num} é igual a 20.')
    elif (num > 20):
        print (f'{num} é maior que 20.')

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q9():
    nasc = int(input('Insira o ano de nascimento: '))
#    ano = int(input('Insira o ano atual: '))
#    if (nasc <= ano):
    if (nasc <= hoje.year): #hoje.year = biblioteca importada antes da q1()
        print(f'{hoje.year-nasc} anos.')
    else:
        print('Dados inválidos.')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    num1 = int(input('1º Número: '))
    num2 = int(input('2º Número: '))
    num3 = int(input('3º Número: '))
    lista = [num1, num2, num3]    
    lista.sort()
    print(lista)

#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    num1 = int(input('1º Número: '))
    num2 = int(input('2º Número: '))
    num3 = int(input('3º Número: '))
    lista = [num1, num2, num3]    
    lista.sort()
    print(f'{lista[2]} é o maior número.')

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos
def q12():
    idade = int(input("Qual é a idade? "))
    if (65 >= idade >= 18):
        print(f'É maior.')
    elif (idade < 18):
        print(f'É menor.')
    elif (idade > 65):
        print('É maior de 65.')

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
def q13():
    nome = input('Nome: ')
    nota1 = float(input('Nota da prova 1:'))
    nota2 = float(input('Nota da prova 2:'))
    media = (nota1 + nota2)/2
    if (media >= 7):
        print (f'Aprovado com média {media}.')
    elif (7 > media >= 3):
        print (f'Média: {media}. \nProva final.')
    else:
        print (f'Média {media}. \nReprovado.')

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
    salario = float(input('Insira o salário em R$: '))
    if (salario <= 600):
        print(f'Salário: {salario}. \nDesconto INSS: Isento.')
    elif (600 < salario <= 1200):
        print (f'Salário: {salario}. \nDesconto INSS: 20%.')
    elif (1200 < salario <= 2000):
        print (f'Salário: {salario}. \nDesconto INSS: 25%.')
    else:
        print (f'Salário: {salario}. \nDesconto INSS: 30%.')
#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
    custo = float(input('Insira custo do produto: R$'))
    if (custo < 20):
        print(f'{custo} + 45% = {custo + (custo*0.45)}')
    else:
        print(f'{custo} + 30% = {custo + (custo*0.30)}')

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
    idade = int(input('Insira a idade: '))
    if ( 5 <= idade <= 7):
        print (f'Categoria: Infantil A.')
    elif ( 8 <= idade <= 10):
        print (f'Categoria: Infantil B.')
    elif ( 11 <= idade <= 13):
        print (f'Categoria: Juvenil A.')
    elif ( 14 <= idade <= 17):
        print (f'Categoria: Juvenil B.')
    elif ( 18 <= idade):
        print (f'Categoria: Sênior.')
    else: 
        print (f'Não compete.')

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def q17():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    if (idade <= 10):
        print (f'Nome: {nome} \nValor: R$30.00')
    elif (10 < idade <= 29 ):
        print (f'Nome: {nome} \nValor: R$60.00')
    elif (29 < idade <= 45 ):
        print (f'Nome: {nome} \nValor: R$120.00')
    elif (45 < idade <= 59 ):
        print (f'Nome: {nome} \nValor: R$150.00')
    elif (59 < idade <= 65 ):
        print (f'Nome: {nome} \nValor: R$250.00')
    else:
        print (f'Nome: {nome} \nValor: R$400.00')

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
# def q18():
#     mes = int(input('Insira o número do mês (de 1 a 12): '))
#     if (mes == 1):
#         print ('Janeiro')
#     elif (mes == 2):
#         print ('Fevereiro')
#     elif (mes == 3):
#         print ('Março')
#     elif (mes == 4):
#         print ('Abril')
#     elif (mes == 5):
#         print ('Maio')
#     elif (mes == 6):
#         print ('Junho')
#     elif (mes == 7):
#         print ('Julho')
#     elif (mes == 8):
#         print ('Agosto')
#     elif (mes == 9):
#         print ('Setembro')
#     elif (mes == 10):
#         print ('Outubro')
#     elif (mes == 11):
#         print ('Novembro')
#     elif (mes == 12):
#         print ('Dezembro')
#     else:
#         print ('Mês inválido!')

def q18():
    mes = int(input('Digite o número do mês: '))
    if mes < 1 or mes > 12:
        print('Mês Inválido!')
    else:
        data = datetime.strptime(f'01/{mes}/24','%d/%m/%y') #criar uma data a prtir do número informado no input (%Y = ano por extenso, %y ano c/ 2 digitos).
        mes_extenso = data.strftime('%B') #escrever o mes por extenso (english), %B mes por extenso, %b mês por extenso abreviado.
        print(tradutor.translate(mes_extenso)) #traduzir o mês. Depende da biblioteca importada no inicio (linha 5).

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
def q19():
    j1 = int(input('Pontuação Jogador 1: '))
    j2 = int(input('Pontuação Jogador 2: '))
    j3 = int(input('Pontuação Jogador 3: '))
    lista = [j1, j2, j3]
    lista.sort(reverse=True)
    print (f'1º: {lista[0]} \n2º: {lista[1]} \n3º: {lista[2]}')
    if (j1+j2+j3) > 100:
        print(f'Média da equipe: {(j1+j2+j3)/3}')
    else:
        print ('Equipe desclassificada!')


#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def q20():
    saldomedio = float(input('Insira o saldo médio: '))
    if (0 <= saldomedio <= 500):
        print (f'Saldo médio: {saldomedio} \nCrédito aprovado: R$00.00')
    elif (501 <= saldomedio <= 1000):
        print (f'Saldo médio: {saldomedio} \nCrédito aprovado: R${round(saldomedio*0.3,2)}')
    elif (1001 <= saldomedio <= 3000):
        print (f'Saldo médio: {saldomedio} \nCrédito aprovado: R${round(saldomedio*0.4,2)}')
    elif (3001 <= saldomedio):
        print (f'Saldo médio: {saldomedio} \nCrédito aprovado: R${round(saldomedio*0.5,2)}')
    else:
        print('Valor inválido.')
        
#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
def q21():
    livro = input('Nome do livro: ')
    usuario = int(input('Tipo de usuário: \n1 - Aluno \n2 - Professor: '))
    if usuário == 1:
        print(f'Nome do livro: {livro} \nTipo de usuário: Aluno \nTotal de dias para devolução: 3')
    elif usuário == 2:
        print(f'Nome do livro: {livro} \nTipo de usuário: Professor \nTotal de dias para devolução: 10')

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def q22():
    percurso = float(input('Insira o tamanho do percurso(km): '))
    tipocarro = int(input('''
    1 - Carro tipo A (12km/L)
    2 - Carro tipo B (9km/L)
    3 - Carro tipo C (8km/L)
    Digite a opção:
    '''))


#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal
def q23():
    prato = int(input('''
        Pratos:
    1 - Vegetariano
    2 - Peixe
    3 - Frango
    4 - Carne
    Digite a opção desejada:
    '''))

    bebida = int(input('''
    Bebidas:
    1 - Chá
    2 - Suco de laranja
    3 - Suco de melão
    4 - Refrigerante diet
    Digite a opção desejada:
    '''))
    
    sobremesa = int(input( '''
    Sobresemas: 
    1 - Abacaxi
    2 - Sorvete diet
    3 - Mousse diet
    4 - Mousse chocolate
    Digite a opção desejada:
    '''))

    cal = 0
    cal += 180 if prato == 1 else 0
    cal += 230 if prato == 2 else 0
    cal += 250 if prato == 3 else 0
    cal += 350 if prato == 4 else 0    
    cal += 20 if bebida == 1 else 0
    cal += 70 if bebida == 2 else 0
    cal += 100 if bebida == 3 else 0
    cal += 65 if bebida == 4 else 0    
    cal += 75 if sobremesa == 1 else 0
    cal += 110 if sobremesa == 2 else 0
    cal += 170 if sobremesa == 3 else 0
    cal += 200 if sobremesa == 4 else 0

    print(f'Total de calorias: {cal}')

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.
def q24():


#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos


questao = int(input('Qual questão executar? '))
eval(f'q{questao}()')
# match questao:
#     case 1:
#         q1 ()
#     case 2:
#         q2 ()
#     case 3:
#         q3 ()
#     case 4:
#         q4 ()
#     case 5:
#         q5 ()
#     case 6:
#         q6 ()
#     case 7:
#         q7 ()
#     case 8:
#         q8 ()
#     case 9:
#         q9 ()
#     case 10:
#         q10 ()
#     case 11:
#         q11 ()
#     case 12:
#         q12 ()
#     case 13:
#         q13 ()
#     case 14:
#         q14 ()
#     case 15:
#         q15 ()
#     case 16:
#         q16 ()
#     case 17:
#         q17 ()
#     case 18:
#         q18 ()
#     case 19:
#         q19 ()
#     case 20:
#         q20 ()
#     case 21:
#         q21 ()
#     case 22:
#         q22 ()
#     case 23:
#         q23 ()
#     case 24:
#         q24 ()
#     case 25:
#         q25 ()
#     case _:
#         print ('Questão inválida!')


#eval = avalia a string como comando python