print('Bem vindo!')
endereco = input('Digite o seu endereço: ')
ano_nasc = input('Digite seu ano de nascimento: ')

while not ano_nasc.isnumeric():
    ano_nasc = input('Deve ser um ano inteiro. Digite seu ano de nascimento: ')

ano_nasc = int(ano_nasc)

if 2024 - ano_nasc < 18:
    print('Você não tem idade para consumir nossos produtos.')
else:
    total = 0
    frete = 0

    quant_um = 0
    quant_dois = 0
    quant_tres = 0

    while True:
        opcoes = '''
            Nossos produtos são:

            1 - Vinho tinto: R$ 25
            2 - Vinho seco: R$ 35
            3 - Hidromel: R$ 50
        '''
        preco = 0

        print(opcoes)
        escolha = input('Qual você deseja? ')

        while not(
            escolha == '1'
            or escolha == '2'
            or escolha == '3'
        ):
            escolha = input('Escolha inválida. Qual você deseja? ')

        quantidade = input('Quantas unidades? ')

        while not quantidade.isnumeric():
            quantidade = input('Deve ser um número. Quantas unidades? ')

        quantidade = int(quantidade)

        if escolha == '1':
            preco += 25
            quant_um += quantidade
        elif escolha == '2':
            preco += 35
            quant_dois += quantidade
        else:
            preco += 50
            quant_tres += quantidade

        total += preco * quantidade

        continuar = input('Deseja continuar comprando? (s/n): ')

        while not(continuar == 's' or continuar == 'n'):
            continuar = input("Deve ser apenas 's' ou 'n'. Deseja continuar? ")

        if continuar == 's':
            continue
        else:
            break

    if total > 500:
        print('Frete grátis!')
    else:
        frete = 5 /100

    total += total * frete

    mensagem = f'''
        Obrigado pela compra!

        Você comprou:
            - {quant_um} unidades de vinho tinto
            - {quant_dois} unidades de vinho seco
            - {quant_tres} unidades de hidromel

        Valor total: R$ {total}
        Frete: {frete * 100}%
        Entrega em: {endereco}
    '''

    print(mensagem)