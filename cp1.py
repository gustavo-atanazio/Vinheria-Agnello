print('Bem vindo!')
idade = int(input('Em qual ano você nasceu? '))

if 2024 - idade < 18:
    print('Você não tem idade para consumir nossos produtos.')
else:
    endereco = input('Qual é o seu endereço? ')

    opcao1 = 'Vinho tinto'
    preco1 = 19.90

    opcao2 = 'Vinho seco'
    preco2 = 25.95

    opcao3 = 'Hidromel'
    preco3 = 55.95

    print('Nossos produtos são:')
    print(f'{opcao1}, preço: R$ {preco1}')
    print(f'{opcao2}, preço: R$ {preco2}')
    print(f'{opcao3}, preço: R$ {preco3}')

    escolha = input('Qual opção você escohe? ')
    quantidade = int(input('Quantas garrafas? '))

    valor = 0
    taxa = 0.25
    total = 0

    if escolha == opcao1:
        valor = preco1 * quantidade
    elif escolha == opcao2:
        valor = preco2 * quantidade
    elif escolha == opcao3:
        valor = preco3 * quantidade
    else:
        print('Sua escolha não está entre nossos produtos.')

    if valor >= 100:
        taxa = 0
        print('Frete grátis!')

    total = valor + (valor * taxa)

    print(f'Obrigado pela compra! O total foi R$ {total: 2f} (incluso frete). A entrega será no endereço: {endereco}')
