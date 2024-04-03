#1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

soma_AB = A + B
print(soma_AB)
if soma_AB < C :
    print ("A soma de A + B é menor que C")
else:
    print ("A soma de A + B é maior que C") 

#2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

Numero = float(input("Digite o seu número: "))
if Numero % 2 == 0 and Numero  < 0:
    print("O número digitado é par e negativo")
elif Numero % 2 == 0 and Numero > 0:
    print("O número digitado é par e positivo")
elif Numero % 2 != 0 and Numero > 0:
    print("O número digitado é impar e positivo")
elif Numero % 2 != 0 and Numero < 0:
    print("O número digitado é impar e negativo")
else:
    print("O número digitado é neutro")
    
#3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores
    
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A == B: 
    C =  A + B 
    print(C)
else:
    C = A * B
    print(C)

#4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.

Numero = int(input("Digite o seu Número: "))
print("O antecessor do seu número é: ", Numero - 1)
print("O Sucessor do seu número é: ", Numero + 1)

#5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

salario_Min = float(input("Digite o valor de A: "))
salario_Usuario = float(input("Digite o valor de B: "))
contador = 0

while salario_Usuario > salario_Min:
    salario_Usuario -= salario_Min
    contador += 1

print ("Você recebe" , contador, " vezes um salário mínimo")

#6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

valor = float(input("Digite o valor: "))
valor_Reajustado = valor * (5/100)
print(f"O Valor reajustado é de: {valor_Reajustado:.2f} ")

#7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.

valor_UM = bool(input("Digite o primeiro valor lógico: "))
valor_DOIS = bool(input("Digite o primeiro valor lógico: "))

if valor_UM  and valor_DOIS:
    print("Os valores são verdadeiros")
else:
    print("Os valores são falsos")

#8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

print ("Digite 3 valores diferentes")
A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))

if A != B and A != C and B != C:
    if A > B and A > C:
        if B > C:
            print(C, B, A)
        else: 
            print(B, C, A)
    elif B > A and B > C:
        if A > C:
            print(C, A, B)
        else: 
            print(A, C, B)  
    elif C > A and C > B:
        if A > B:
            print(B, A, C) 
        else: 
            print(A, B, C)

else:
    print("Os valores devem ser diferentes.")

#9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 

peso = float(input("Digite o seu peso: "))
altura =  float(input("Digite a sua altura: "))

imc = peso * (altura * altura)

if imc <= 18.5 :
    print("Abaixo do peso ideal")
if imc > 18.5 and imc <= 24.9 :
    print("Você está no peso ideal, parabéns!")
if imc >= 25.0 and imc <= 29.9 :
    print("Levemente a cima do peso")
if imc >= 30.0 and imc <= 34.9 :
    print("Obesidade grau I")
if imc >= 35.0 and imc <= 39.9 :
    print("Obesidade grau II (severa)")
if imc >= 40 :
    print("Obesidade grau III (mórbida)")

 #10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.

nota_Um = float(input("Digite sua primeira nota: "))
nota_Dois = float(input("Digite sua segunda nota: "))
nota_Tres = float(input("Digite sua terceira nota: "))

media = (nota_Um + nota_Dois + nota_Tres)/ 3

print(f"A sua média é: {media:.2f}")

#11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.
nome_Aluno = str(input("Digite seu nome: "))
nota_Um = float(input("Digite sua primeira nota: "))
nota_Dois = float(input("Digite sua segunda nota: "))
nota_Tres = float(input("Digite sua terceira nota: "))
nota_Quatro = float(input("Digite sua quarta nota: "))

media = (nota_Um + nota_Dois + nota_Tres + nota_Quatro)/ 4

if media >= 7 :
    print(f"{nome_Aluno} parabéns, você foi aprovado! Sua média é: {media:.2f}")

else:
    print(f"{nome_Aluno} Você foi reprovado, sua média é: {media:.2f}")

 #12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado

#Tabela de Código de Condições de Pagamento

 

 #1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

# 2 - À Vista no cartão de crédito, recebe 10% de desconto

 #3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

 #4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
    
valor_Produto = float(input("Digite o valor do produto: "))

print("Qual sua forma de Pagamento \n")
forma_Pagamento = int(input(" Digite 1 para  dinheiro ou pix. Digite 2 para  cartão de crédito. Digite 3 para  parcelar em 2x no cartão. Digite 4 para  parcelar em 3x ou mais no cartão"))

if forma_Pagamento > 0 and forma_Pagamento <= 4:
    if forma_Pagamento == 1:
        valor_Produto -= valor_Produto * 0.15
        print(f"O Valor da sua compra é de: {valor_Produto:.2f}")
    elif forma_Pagamento == 2:
        valor_Produto -= valor_Produto * 0.10
        print(f"O Valor da sua compra é de: {valor_Produto:.2f}")
    elif forma_Pagamento == 3:
        print(f"O Valor da sua compra é de: {valor_Produto:.2f}")
    else:
        valor_Produto += (valor_Produto * 0.1)
else:
    print("Você não escolheu uma opção de pagamento válida")

#13 - Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 
    
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome}, você é maior de idade")
else:
    print(f"{nome}, você é menor de idade")

#14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.
    
valor_A = float(input("Digite um valor: "))
valor_B = float(input("Digite outro valor: "))

valor_C= valor_B
valor_B = valor_A
valor_A = valor_C

print(valor_A)
print(valor_B)

#15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em consideração o ano com 365 dias e o mês com 30 dias.

#(Ex: 5 anos, 2 meses e 15 dias de vida)
import datetime
ano_Nasceu = int(input("Digite o ano que você nasceu: "))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_Nasceu
meses_Vividos = idade * 12
dias_Vividos = idade * 365

print("Esta pessoa viveu aproximadamente:")
print("Anos:", idade)
print("Meses:", meses_Vividos)
print("Dias:", dias_Vividos)

#16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é equilátero, isósceles ou escaleno.

a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("O triângulo é Equilátero")
    elif a == b != c or b == c != a or a == c != b:
         print("O triângulo é isósceles")
    else:
        print("O triângulo é Escaleno")
else:
    print("Esses valores não formam um triângulo")

#17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

#Fórmula: C = (5 * ( F-32) / 9)

temperatura_Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
temperatura_Celsius = (5*(temperatura_Fahrenheit-32)/9)

print(f"A temperatura em Fahrenheit é: {temperatura_Fahrenheit:.1f}")
print(f"A temperatura em Celsius é: {temperatura_Celsius:.1f}")

#18 - Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano. 
#Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Francisco seja menor que Sara.

altura_F = 1.50
altura_S = 1.10
ano = 0
while altura_F >= altura_S:
    altura_F += 0.02
    altura_S += 0.03
    ano += 1

print(f"{ano} anos são necessários.")

#19 - Faça um algoritmo que imprima na tela a tabuada de 1 até 10.
    
for i in range(1, 11):
    print(f"Tabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print() 

#20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

numero = int(input("Digite um número inteiro: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

 #21 - Faça um algoritmo que mostre um valor aleatório entre 0 e 100.
    
import random

numero_aleatorio = random.randint(0, 100)
print(numero_aleatorio)

#22 - Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o quociente e o resto da divisão inteira entre eles.

A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))

if B != 0:
    print(A / B)
    print(int(A % B))
else: 
    print("Não é possível dividir por zero.")

#21 - Faça um algoritmo que efetue o cálculo do salário líquido de um professor. As informações fornecidas serão: valor da hora aula, número de aulas lecionadas no mês e percentual de desconto do INSS. Imprima na tela o salário líquido final.

valor_Hora_Aula = float(input("Digite o valor da hora-aula: "))
num_Aulas_Mes = int(input("Digite o número de aulas lecionadas no mês: "))
percentual_Desconto_Inss = float(input("Digite o percentual de desconto do INSS (em %): "))

salario_Bruto = valor_Hora_Aula * num_Aulas_Mes

desconto_Inss = salario_Bruto * (percentual_Desconto_Inss / 100)

salario_Liquido = salario_Bruto - desconto_Inss

print("O salário líquido final do professor é:", salario_Liquido)

#22 - Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o carro faz 12km com um litro. Deve-se fornecer ao usuário o tempo que será gasto na viagem a sua velocidade média, distância percorrida e a quantidade de litros utilizados para fazer a viagem.

#Fórmula: distância = tempo x velocidade.

            #litros usados = distância / 12.

tempo = float(input("Digite quanto tempo dura a viagem em horas: "))
velocidade_Media = float(input("Digite a velocidade média durante a viagem em km/h: "))
distancia = tempo * velocidade_Media
litros_Utilizados = distancia / 12

print(f"Distância percorrida: {distancia} km")
print(f"Litros de combustivel utilizados: {litros_Utilizados} litros")
