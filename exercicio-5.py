print('------- DESAFIO 05 --------')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
sucessor = (n1 + n2) + (1)
antecessor = (n1 + n2) - (1)
d = n1 // n2
m = n1 * n2
print('A soma dos seus números são {} e seu sucessor é {} e seu antecessor é {} e a divisão {} e a multiplicação {},'.format(s, sucessor, antecessor, d, m))


print('------- DESAFIO 07 --------')

n1 = int(input('Digite um número '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

print('O dobro do seu número é {}, o triplo é {} e a raiz quadrada é {:.3f}'.format(d, t, r))


print('------- DESAFIO 07 --------')

nt1 = int(input('Digite a sua primeira nota '))
nt2 = int(input('Digite a sua segunda nota '))
md = (nt1 + nt2) / 2
print('A média das suas notas são {}'.format(md))


print('------- DESAFIO 08 --------')

c = int(input('Digite um valor em METROS para ser convertido em centimetros e milimetros '))
cm = c * 100
mm = c * 1000

print('O valor convertido em METROS para centimetros {} e o valor para milimetros {}'.format(cm, mm))


print('------- DESAFIO 09 --------')

print('Vamos lá, agora precisamos criar uma nuada')
n = int(input('Escolha um número para fazermos sua nuada de 0 à 10:'))
n0 = n*0
n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10
print('A Tabuada resultante é:\n {}x0={} \n {}x1={} \n {}x2={} \n {}x3={} \n {}x4={} \n {}x5={} \n {}x6={} \n {}x7={} \n {}x8={} \n {}x9={} \n {}x10={}'.format(n,n0,n,n1,n,n2,n,n3,n,n4,n,n5,n,n6,n,n7,n,n8,n,n9,n,n10))


print('------- DESAFIO 10 --------')
r = float(input('Digite o valor em reais para converter para Dólar '))
conversao = r/4.50
print('O valor de {:.2f} em reais equivale a {:.2f} dólares.'.format(r,conversao))


print('------- DESAFIO 11 --------')

m1 = float(input('Digite a largura em Metros '))
m2 = float(input('Digite a altura em Metros '))
area = m1 * m2

print('A área da parede é de {:.1f} metros quadrados'.format(area))

tinta = area/2

print('Você então precisará de {:.1f} litros de tinta'.format(tinta))


print('------- DESAFIO 12 --------')

product = float(input('Qual é o preço do produto? '))
discount = product - (product * 5/100)

print('O valor do produto é de {} e com desconto de 5% fica acessivel á {}'.format(product, discount))


print('------- DESAFIO 13 --------')

salario = float(input('Digite seu salário '))
newsalario = salario + (salario * 15 / 100)

print('Seu salário é {:.2f} e seu novo salário com 15% de aumento é {:.2f}'.format(salario, newsalario))

