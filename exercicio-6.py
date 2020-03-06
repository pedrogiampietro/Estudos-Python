dadoskm = float(input('Qual a quantidade de KM percorridos desde que alugou o carro? '))

dadosdays = int(input('Qual a quantidade de dias que você alugou carro? '))

days = dadosdays * 60
km = dadoskm * 0.15
results = days + km
print('Você pagará R${:.2f} por {:.2f} kms utilizados. '.format(km, dadoskm))
print('E R${:.2f} por {:.0f} dias alugados. \n O total da sua conta é: {}'.format(days, dadosdays, results))


