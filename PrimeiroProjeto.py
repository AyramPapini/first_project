nome = input('Digite seu nome: ')

# Variáveis

opcao = 1
opcaomat = 0
num = 1

# Menu de opções gerais
print('\nSeja bem-vindo, {}!'.format(nome))
while opcao != 0:
    opcao = int(input(
        '\nPor favor, selecione uma opção:\n[1] Operações Matemáticas\n[2] Para ver seu nome ou palavra ao contrário\n[3] Calcular IMC'
        '\n[4] Conversão entre Dólar e Real\n[5] Conversão de Medidas\n[0] Sair\n'))

    if opcao == 0:
        break

    # Opção 1, Menu de opções matemáticas

    if opcao == 1:
        print(
            '\nQual operação deseja fazer? \n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potenciação')
        opcaomat = int(input(': '))

        # Laços de comparação e execução das operações de acordo com a escolha do usuário

        if opcaomat == 1:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite outro número: '))
            soma = num1 + num2
            print('O resultado da soma é: {} + {} = {}'.format(num1, num2, soma))
            num = int(input('\nDigite 0 para voltar'))
        elif opcaomat == 2:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite outro número: '))
            sub = num1 - num2
            print('O resultado da subtração é: {}'.format(sub))
            num = int(input('\nDigite 0 para voltar'))
        elif opcaomat == 3:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite outro número: '))
            mult = num1 * num2
            print('O resultado da multiplicação é: {}'.format(mult))
            num = int(input('\nDigite 0 para voltar'))
        elif opcaomat == 4:
            num1 = int(input('Digite um número: '))
            num2 = int(input('Digite outro número: '))
            div = num1 / num2
            print('O resultado da divisão é: {}'.format(div))
            num = int(input('\nDigite 0 para voltar'))
        elif opcaomat == 5:
            num1 = int(input('Digite o número Base: '))
            num2 = int(input('Digite o Expoente: '))
            pot = num1 ** num2
            print('O resultado da potenciação é: {}'.format(pot))
            num = int(input('\nDigite 0 para voltar'))



    # Opção 2 Nome ao contrário, o usuário pode inserir o próprio nome ou qualquer outra palavra para inverter

    elif opcao == 2:
        novonome = input('Digite um nome ou palavra para ver ao contrário: ')
        print('\nSeu nome ao contrário é {}'.format(novonome.upper()[::-1]))

    # Opção 3 IMC, calcula o IMC de acordo com as informações inseridas pelo usuário(peso e altura)

    elif opcao == 3:
        peso = float(input('Digite o seu peso: '))
        altura = float(input('Digite sua altura (cm): '))
        imc = peso / (altura ** 2)
        if imc < 18.5:
            print('Seu imc é: {:.1f} Peso Baixo'.format(imc))
        elif imc >= 18.5 and imc <= 24.9:
            print('Seu imc é: {:.1f} Peso Normal'.format(imc))
        elif imc >= 25.0 and imc <= 29.9:
            print('Seu imc é: {:.1f} Sobrepeso'.format(imc))
        elif imc >= 30.0 and imc <= 34.9:
            print('Seu imc é: {:.1f} Obesidade (Grau I)'.format(imc))
        elif imc >= 35.0 and imc <= 39.9:
            print('Seu imc é: {:.1f} Obesidade Severa (Grau II)'.format(imc))
        elif imc >= 40:
            print('Seu imc é: {:.1f} Obesidade Mórbida (Grau III)'.format(imc))
        num = int(input('\nDigite 0 para voltar'))

    # Opção 4 Conversor, converte o valor inserido em Real para Dólar

    elif opcao == 4:

        dinheiro = float(input('Digite o valor em Real que deseja converter para Dolar: R$ '))
        dinheiroconv = dinheiro / 5.37
        print('A cotação utilizada foi do dia 11/02/2021 onde o Dolar estava $ 5,37')
        print('Com R${:.2f} reais você pode comprar ${:.2f} dólares'.format(dinheiro, dinheiroconv))
        num = int(input('\nDigite 0 para voltar'))

    elif opcao == 5:
        escmedida = int(
            input('Selecione a unidade a ser convertida \n[1]Comprimento\n[2]Massa\n[3]Tempo\n[4]Temperatura\n'))

            # Laço para converter Comprimento

        if escmedida == 1:
            comp1 = int(input(
                'Deseja converter de \n[1] Milimetro\n[2] Centímetro\n[3] Decimetro\n[4] Metro\n[5] Decâmetro\n[6] Hectometro\n[7] Quilometro\n'))
            comp2 = int(input(
                'Para \n[1] Milimetro\n[2] Centímetro\n[3] Decimetro\n[4] Metro\n[5] Decâmetro\n[6] Hectometro\n[7] Quilometro\n'))

            if comp1 == 1 and comp2 == 2:
                valorconv = float(input('Digite o valor em Milimetros(mm): '))
                conv = valorconv / 10
                print('{}mm equivalem a {:.2f}cm'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 3:
                valorconv = float(input('Digite o valor em Milimetros(mm): '))
                conv = valorconv / 100
                print('{}mm equivalem a {:.2f}dm'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 4:
                valorconv = float(input('Digite o valor em Milimetros(mm): '))
                conv = valorconv / 1000
                print('{}mm equivalem a {:.2f}m'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 5:
                valorconv = float(input('Digite o valor em Milimetros(mm): '))
                conv = valorconv / 10000
                print('{}mm equivalem a {:.2f}dam'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 6:
                valorconv = float(input('Digite o valor em Milimetros(mm): '))
                conv = valorconv / 100000
                print('{}mm equivalem a {:.2f}hm'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 7:
                valorconv = float(input('Digite o valor em Milimetros(mm): '))
                conv = valorconv / 1000000
                print('{}mm equivalem a {:.2f}km'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 1:
                print('Você não pode converter Milimetros em Milimetros, escolha outra opção.')

            if comp1 == 2 and comp2 == 1:
                valorconv = float(input('Digite o valor em Centímetros(cm): '))
                conv = valorconv * 10
                print('{}cm equivalem a {:.2f}mm'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 3:
                valorconv = float(input('Digite o valor em Centímetros(cm): '))
                conv = valorconv / 10
                print('{}cm equivalem a {:.2f}dm'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 4:
                valorconv = float(input('Digite o valor em Centímetros(cm): '))
                conv = valorconv / 100
                print('{}cm equivalem a {:.2f}m'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 5:
                valorconv = float(input('Digite o valor em Centímetros(cm): '))
                conv = valorconv / 1000
                print('{}cm equivalem a {:.2f}dam'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 6:
                valorconv = float(input('Digite o valor em Centímetros(cm): '))
                conv = valorconv / 10000
                print('{}cm equivalem a {:.2f}hm'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 7:
                valorconv = float(input('Digite o valor em Centímetros(cm): '))
                conv = valorconv / 100000
                print('{}cm equivalem a {:.2f}km'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 2:
                print('Você não pode converter Centimetros em Centimetros, escolha outra opção.')

            if comp1 == 3 and comp2 == 1:
                valorconv = float(input('Digite o valor em Decímetros(dm): '))
                conv = valorconv * 100
                print('{}dm equivalem a {:.2f}mm'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 2:
                valorconv = float(input('Digite o valor em Decímetros(dm): '))
                conv = valorconv * 10
                print('{}dm equivalem a {:.2f}cm'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 4:
                valorconv = float(input('Digite o valor em Decímetros(dm): '))
                conv = valorconv / 10
                print('{}dm equivalem a {:.2f}m'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 5:
                valorconv = float(input('Digite o valor em Decímetros(dm): '))
                conv = valorconv / 100
                print('{}dm equivalem a {:.2f}dam'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 6:
                valorconv = float(input('Digite o valor em Decímetros(dm): '))
                conv = valorconv / 1000
                print('{}dm equivalem a {:.2f}hm'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 7:
                valorconv = float(input('Digite o valor em Decímetros(dm): '))
                conv = valorconv / 10000
                print('{}dm equivalem a {:.2f}km'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 3:
                print('Você não pode converter Decimetros em Decimetros, escolha outra opção.')

            if comp1 == 4 and comp2 == 1:
                valorconv = float(input('Digite o valor em Metros(m): '))
                conv = valorconv * 1000
                print('{}m equivalem a {:.2f}mm'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 2:
                valorconv = float(input('Digite o valor em Metros(m): '))
                conv = valorconv * 100
                print('{}m equivalem a {:.2f}cm'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 3:
                valorconv = float(input('Digite o valor em Metros(m): '))
                conv = valorconv * 10
                print('{}m equivalem a {:.2f}dm'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 5:
                valorconv = float(input('Digite o valor em Metros(m): '))
                conv = valorconv / 10
                print('{}m equivalem a {:.2f}dam'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 6:
                valorconv = float(input('Digite o valor em Metros(m): '))
                conv = valorconv / 100
                print('{}m equivalem a {:.2f}hm'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 7:
                valorconv = float(input('Digite o valor em Metros(m): '))
                conv = valorconv / 1000
                print('{}m equivalem a {:.2f}km'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 4:
                print('Você não pode converter Metros em Metros, escolha outra opção.')

            if comp1 == 5 and comp2 == 1:
                valorconv = float(input('Digite o valor em Decâmetros(dam): '))
                conv = valorconv * 10000
                print('{}dam equivalem a {:.2f}mm'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 2:
                valorconv = float(input('Digite o valor em Decâmetros(dam): '))
                conv = valorconv * 1000
                print('{}dam equivalem a {:.2f}cm'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 3:
                valorconv = float(input('Digite o valor em Decâmetros(dam): '))
                conv = valorconv * 100
                print('{}dam equivalem a {:.2f}dm'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 4:
                valorconv = float(input('Digite o valor em Decâmetros(dam): '))
                conv = valorconv * 10
                print('{}dam equivalem a {:.2f}m'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 6:
                valorconv = float(input('Digite o valor em Decâmetros(dam): '))
                conv = valorconv / 10
                print('{}dam equivalem a {:.2f}hm'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 7:
                valorconv = float(input('Digite o valor em Decâmetros(dam): '))
                conv = valorconv / 100
                print('{}dam equivalem a {:.2f}km'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 5:
                print('Você não pode converter Decâmetros em Decâmetros, escolha outra opção.')

            if comp1 == 6 and comp2 == 1:
                valorconv = float(input('Digite o valor em Hectômetros(hm): '))
                conv = valorconv * 100000
                print('{}hm equivalem a {:.2f}mm'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 2:
                valorconv = float(input('Digite o valor em Hectômetros(hm): '))
                conv = valorconv * 10000
                print('{}hm equivalem a {:.2f}cm'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 3:
                valorconv = float(input('Digite o valor em Hectômetros(hm): '))
                conv = valorconv * 1000
                print('{}hm equivalem a {:.2f}dm'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 4:
                valorconv = float(input('Digite o valor em Hectômetros(hm): '))
                conv = valorconv * 100
                print('{}hm equivalem a {:.2f}m'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 5:
                valorconv = float(input('Digite o valor em Hectômetros(hm): '))
                conv = valorconv * 10
                print('{}hm equivalem a {:.2f}dam'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 7:
                valorconv = float(input('Digite o valor em Hectômetros(hm): '))
                conv = valorconv / 10
                print('{}hm equivalem a {:.2f}km'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 6:
                print('Você não pode converter Hectômetros em Hectômetros, escolha outra opção.')

            if comp1 == 7 and comp2 == 1:
                valorconv = float(input('Digite o valor em Quilômetros(km): '))
                conv = valorconv * 1000000
                print('{}km equivalem a {:.2f}mm'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 2:
                valorconv = float(input('Digite o valor em Quilômetros(km): '))
                conv = valorconv * 100000
                print('{}km equivalem a {:.2f}cm'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 3:
                valorconv = float(input('Digite o valor em Quilômetros(km): '))
                conv = valorconv * 10000
                print('{}km equivalem a {:.2f}dm'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 4:
                valorconv = float(input('Digite o valor em Quilômetros(km): '))
                conv = valorconv * 1000
                print('{}km equivalem a {:.2f}m'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 5:
                valorconv = float(input('Digite o valor em Quilômetros(km): '))
                conv = valorconv * 100
                print('{}km equivalem a {:.2f}dam'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 6:
                valorconv = float(input('Digite o valor em Quilômetros(km): '))
                conv = valorconv * 10
                print('{}km equivalem a {:.2f}hm'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 7:
                print('Você não pode converter Quilômetros em Quilômetros, escolha outra opção.')

            # Laço para converter Massa

        elif escmedida == 2:
            comp1 = int(input(
                'Deseja converter de \n[1] Miligrama(mg)\n[2] Centigrama(cg)\n[3] Decigrama(dg)\n[4] Grama(g)\n[5] Decagrama(dag)\n[6] Hectograma(hg)\n[7] Quilograma(kg)\n'))
            comp2 = int(input(
                'Para \n[1] Miligrama\n[2] Centigrama\n[3] Decigrama\n[4] Grama\n[5] Decagrama\n[6] Hectograma\n[7] Quilograma\n'))

            if comp1 == 1 and comp2 == 2:
                valorconv = float(input('Digite o valor em Miligrama(mg): '))
                conv = valorconv / 10
                print('{}mg equivalem a {:.2f}cg'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 3:
                valorconv = float(input('Digite o valor em Miligrama(mg): '))
                conv = valorconv / 100
                print('{}mg equivalem a {:.2f}dg'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 4:
                valorconv = float(input('Digite o valor em Miligrama(mg): '))
                conv = valorconv / 1000
                print('{}mg equivalem a {:.2f}g'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 5:
                valorconv = float(input('Digite o valor em Miligrama(mg): '))
                conv = valorconv / 10000
                print('{}mg equivalem a {:.2f}dag'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 6:
                valorconv = float(input('Digite o valor em Miligrama(mg): '))
                conv = valorconv / 100000
                print('{}mg equivalem a {:.2f}hg'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 7:
                valorconv = float(input('Digite o valor em Miligrama(mg): '))
                conv = valorconv / 1000000
                print('{}mg equivalem a {:.2f}kg'.format(valorconv, conv))
            elif comp1 == 1 and comp2 == 1:
                print('Você não pode converter Miligramas em Miligramas, escolha outra opção.')

            if comp1 == 2 and comp2 == 1:
                valorconv = float(input('Digite o valor em Centigrama(cg): '))
                conv = valorconv * 10
                print('{}cg equivalem a {:.2f}mg'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 3:
                valorconv = float(input('Digite o valor em Centigrama(cg): '))
                conv = valorconv / 10
                print('{}cg equivalem a {:.2f}dg'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 4:
                valorconv = float(input('Digite o valor em Centigrama(cg): '))
                conv = valorconv / 100
                print('{}cg equivalem a {:.2f}g'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 5:
                valorconv = float(input('Digite o valor em Centigrama(cg): '))
                conv = valorconv / 1000
                print('{}cg equivalem a {:.2f}dag'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 6:
                valorconv = float(input('Digite o valor em Centigrama(cg): '))
                conv = valorconv / 10000
                print('{}cg equivalem a {:.2f}hg'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 7:
                valorconv = float(input('Digite o valor em Centigrama(cg): '))
                conv = valorconv / 100000
                print('{}cg equivalem a {:.2f}kg'.format(valorconv, conv))
            elif comp1 == 2 and comp2 == 2:
                print('Você não pode converter Centigramas em Centigramas, escolha outra opção.')

            if comp1 == 3 and comp2 == 1:
                valorconv = float(input('Digite o valor em Decigrama(dg): '))
                conv = valorconv * 100
                print('{}dg equivalem a {:.2f}mg'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 2:
                valorconv = float(input('Digite o valor em Decigrama(dg): '))
                conv = valorconv * 10
                print('{}dg equivalem a {:.2f}cg'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 4:
                valorconv = float(input('Digite o valor em Decigrama(dg): '))
                conv = valorconv / 10
                print('{}dg equivalem a {:.2f}g'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 5:
                valorconv = float(input('Digite o valor em Decigrama(dg): '))
                conv = valorconv / 100
                print('{}dg equivalem a {:.2f}dag'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 6:
                valorconv = float(input('Digite o valor em Decigrama(dg): '))
                conv = valorconv / 1000
                print('{}dg equivalem a {:.2f}hg'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 7:
                valorconv = float(input('Digite o valor em Decigrama(dg): '))
                conv = valorconv / 10000
                print('{}dg equivalem a {:.2f}kg'.format(valorconv, conv))
            elif comp1 == 3 and comp2 == 3:
                print('Você não pode converter Decigramas em Decigramas, escolha outra opção.')

            if comp1 == 4 and comp2 == 1:
                valorconv = float(input('Digite o valor em Grama(g): '))
                conv = valorconv * 1000
                print('{}g equivalem a {:.2f}mg'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 2:
                valorconv = float(input('Digite o valor em Grama(g): '))
                conv = valorconv * 100
                print('{}g equivalem a {:.2f}cg'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 3:
                valorconv = float(input('Digite o valor em Grama(g): '))
                conv = valorconv * 10
                print('{}g equivalem a {:.2f}dg'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 5:
                valorconv = float(input('Digite o valor em Grama(g): '))
                conv = valorconv / 10
                print('{}g equivalem a {:.2f}dag'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 6:
                valorconv = float(input('Digite o valor em Grama(g): '))
                conv = valorconv / 100
                print('{}g equivalem a {:.2f}hg'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 7:
                valorconv = float(input('Digite o valor em Grama(g): '))
                conv = valorconv / 1000
                print('{}g equivalem a {:.2f}kg'.format(valorconv, conv))
            elif comp1 == 4 and comp2 == 4:
                print('Você não pode converter Gramas em Gramas, escolha outra opção.')

            if comp1 == 5 and comp2 == 1:
                valorconv = float(input('Digite o valor em Decagrama(dag): '))
                conv = valorconv * 10000
                print('{}dag equivalem a {:.2f}mg'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 2:
                valorconv = float(input('Digite o valor em Decagrama(dag): '))
                conv = valorconv * 1000
                print('{}dag equivalem a {:.2f}cg'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 3:
                valorconv = float(input('Digite o valor em Decagrama(dag): '))
                conv = valorconv * 100
                print('{}dag equivalem a {:.2f}dg'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 4:
                valorconv = float(input('Digite o valor em Decagrama(dag): '))
                conv = valorconv * 10
                print('{}dag equivalem a {:.2f}g'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 6:
                valorconv = float(input('Digite o valor em Decagrama(dag): '))
                conv = valorconv / 10
                print('{}dag equivalem a {:.2f}hg'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 7:
                valorconv = float(input('Digite o valor em Decagrama(dag): '))
                conv = valorconv / 100
                print('{}dag equivalem a {:.2f}kg'.format(valorconv, conv))
            elif comp1 == 5 and comp2 == 5:
                print('Você não pode converter Decagramas em Decagramas, escolha outra opção.')

            if comp1 == 6 and comp2 == 1:
                valorconv = float(input('Digite o valor em Hectograma(hg): '))
                conv = valorconv * 100000
                print('{}hg equivalem a {:.2f}mg'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 2:
                valorconv = float(input('Digite o valor em Hectograma(hg): '))
                conv = valorconv * 10000
                print('{}hg equivalem a {:.2f}cg'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 3:
                valorconv = float(input('Digite o valor em Hectograma(hg): '))
                conv = valorconv * 1000
                print('{}hg equivalem a {:.2f}dg'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 4:
                valorconv = float(input('Digite o valor em Hectograma(hg): '))
                conv = valorconv * 100
                print('{}hg equivalem a {:.2f}g'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 5:
                valorconv = float(input('Digite o valor em Hectograma(hg): '))
                conv = valorconv * 10
                print('{}hg equivalem a {:.2f}dag'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 7:
                valorconv = float(input('Digite o valor em Hectograma(hg): '))
                conv = valorconv / 10
                print('{}hg equivalem a {:.2f}kg'.format(valorconv, conv))
            elif comp1 == 6 and comp2 == 6:
                print('Você não pode converter Hectogramas em Hectogramas, escolha outra opção.')

            if comp1 == 7 and comp2 == 1:
                valorconv = float(input('Digite o valor em Quilogramas(kg): '))
                conv = valorconv * 1000000
                print('{}kg equivalem a {:.2f}mg'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 2:
                valorconv = float(input('Digite o valor em Quilogramas(kg): '))
                conv = valorconv * 100000
                print('{}kg equivalem a {:.2f}cg'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 3:
                valorconv = float(input('Digite o valor em Quilogramas(kg): '))
                conv = valorconv * 10000
                print('{}kg equivalem a {:.2f}dg'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 4:
                valorconv = float(input('Digite o valor em Quilogramas(kg): '))
                conv = valorconv * 1000
                print('{}kg equivalem a {:.2f}g'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 5:
                valorconv = float(input('Digite o valor em Quilogramas(kg): '))
                conv = valorconv * 100
                print('{}kg equivalem a {:.2f}dag'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 6:
                valorconv = float(input('Digite o valor em Quilogramas(kg): '))
                conv = valorconv * 10
                print('{}kg equivalem a {:.2f}hg'.format(valorconv, conv))
            elif comp1 == 7 and comp2 == 7:
                print('Você não pode converter Quilogramas em Quilogramas, escolha outra opção.')

        # Laço para converter Tempo

        elif escmedida == 3:
            tempo1 = int(input(
                'Deseja converter de \n[1] Segundos\n[2] Minutos\n[3] Horas\n[4] Dias\n[5] Semanas\n[6] Meses\n[7] Anos\n'))
            tempo2 = int(
                input('Para \n[1] Segundos\n[2] Minutos\n[3] Horas\n[4] Dias\n[5] Semanas\n[6] Meses\n[7] Anos\n'))

            if tempo1 == 1 and tempo2 == 2:
                valorconv = int(input('Digite o tempo em Segundos: '))
                conv = valorconv / 60
                print('{} segundos equivalem a {:.2f} minutos'.format(valorconv, conv))
            elif tempo1 == 1 and tempo2 == 3:
                valorconv = int(input('Digite o tempo em Segundos: '))
                conv = valorconv / 3600
                print('{} segundos equivalem a {:.2f} horas'.format(valorconv, conv))
            elif tempo1 == 1 and tempo2 == 4:
                valorconv = int(input('Digite o tempo em Segundos: '))
                conv = valorconv / 86400
                print('{} segundos equivalem a {:.2f} dias'.format(valorconv, conv))
            elif tempo1 == 1 and tempo2 == 5:
                valorconv = int(input('Digite o tempo em Segundos: '))
                conv = valorconv / 604800
                print('{} segundos equivalem a {:.2f} semanas'.format(valorconv, conv))
            elif tempo1 == 1 and tempo2 == 6:
                valorconv = int(input('Digite o tempo em Segundos: '))
                conv = valorconv / 2629800
                print('{} segundos equivalem a {:.2f} meses'.format(valorconv, conv))
            elif tempo1 == 1 and tempo2 == 7:
                valorconv = int(input('Digite o tempo em Segundos: '))
                conv = valorconv / 31536000
                print('{} segundos equivalem a {:.2f} anos'.format(valorconv, conv))
            elif tempo1 == 1 and tempo2 == 1:
                print('Você não pode converter Segundos em Segundos, escolha outra opção.')

            if tempo1 == 2 and tempo2 == 1:
                valorconv = int(input('Digite o tempo em Minutos: '))
                conv = valorconv * 60
                print('{} minutos equivalem a {:.2f} segundos'.format(valorconv, conv))
            elif tempo1 == 2 and tempo2 == 3:
                valorconv = int(input('Digite o tempo em Minutos: '))
                conv = valorconv / 60
                print('{} minutos equivalem a {:.2f} horas'.format(valorconv, conv))
            elif tempo1 == 2 and tempo2 == 4:
                valorconv = int(input('Digite o tempo em Minutos: '))
                conv = valorconv / 1440
                print('{} minutos equivalem a {:.2f} dias'.format(valorconv, conv))
            elif tempo1 == 2 and tempo2 == 5:
                valorconv = int(input('Digite o tempo em Minutos: '))
                conv = valorconv / 10080
                print('{} minutos equivalem a {:.2f} semanas'.format(valorconv, conv))
            elif tempo1 == 2 and tempo2 == 6:
                valorconv = int(input('Digite o tempo em Minutos: '))
                conv = valorconv / 43830
                print('{} minutos equivalem a {:.2f} meses'.format(valorconv, conv))
            elif tempo1 == 2 and tempo2 == 7:
                valorconv = int(input('Digite o tempo em Minutos: '))
                conv = valorconv / 525960
                print('{} minutos equivalem a {:.2f} anos'.format(valorconv, conv))
            elif tempo1 == 2 and tempo2 == 2:
                print('Você não pode converter Minutos em Minutos, escolha outra opção.')

            if tempo1 == 3 and tempo2 == 1:
                valorconv = int(input('Digite o tempo em Horas: '))
                conv = valorconv * 3600
                print('{} horas equivalem a {:.2f} segundos'.format(valorconv, conv))
            elif tempo1 == 3 and tempo2 == 2:
                valorconv = int(input('Digite o tempo em Horas: '))
                conv = valorconv * 60
                print('{} horas equivalem a {:.2f} minutos'.format(valorconv, conv))
            elif tempo1 == 3 and tempo2 == 4:
                valorconv = int(input('Digite o tempo em Horas: '))
                conv = valorconv / 24
                print('{} horas equivalem a {:.2f} dias'.format(valorconv, conv))
            elif tempo1 == 3 and tempo2 == 5:
                valorconv = int(input('Digite o tempo em Horas: '))
                conv = valorconv / 168
                print('{} horas equivalem a {:.2f} semanas'.format(valorconv, conv))
            elif tempo1 == 3 and tempo2 == 6:
                valorconv = int(input('Digite o tempo em Horas: '))
                conv = valorconv / 730.5
                print('{} horas equivalem a {:.2f} meses'.format(valorconv, conv))
            elif tempo1 == 3 and tempo2 == 7:
                valorconv = int(input('Digite o tempo em Horas: '))
                conv = valorconv / 8766
                print('{} horas equivalem a {:.2f} anos'.format(valorconv, conv))
            elif tempo1 == 3 and tempo2 == 3:
                print('Você não pode converter Horas em Horas, escolha outra opção.')

            if tempo1 == 4 and tempo2 == 1:
                valorconv = int(input('Digite o tempo em Dias: '))
                conv = valorconv * 86400
                print('{} dias equivalem a {:.2f} segundos'.format(valorconv, conv))
            elif tempo1 == 4 and tempo2 == 2:
                valorconv = int(input('Digite o tempo em Dias: '))
                conv = valorconv * 1440
                print('{} dias equivalem a {:.2f} minutos'.format(valorconv, conv))
            elif tempo1 == 4 and tempo2 == 3:
                valorconv = int(input('Digite o tempo em Dias: '))
                conv = valorconv * 24
                print('{} dias equivalem a {:.2f} horas'.format(valorconv, conv))
            elif tempo1 == 4 and tempo2 == 5:
                valorconv = int(input('Digite o tempo em Dias: '))
                conv = valorconv / 7
                print('{} dias equivalem a {:.2f} semanas'.format(valorconv, conv))
            elif tempo1 == 4 and tempo2 == 6:
                valorconv = int(input('Digite o tempo em Dias: '))
                conv = valorconv / 30.44
                print('{} dias equivalem a {:.2f} meses'.format(valorconv, conv))
            elif tempo1 == 4 and tempo2 == 7:
                valorconv = int(input('Digite o tempo em Dias: '))
                conv = valorconv / 365.25
                print('{} dias equivalem a {:.2f} anos'.format(valorconv, conv))
            elif tempo1 == 4 and tempo2 == 4:
                print('Você não pode converter Dias em Dias, escolha outra opção.')

            if tempo1 == 5 and tempo2 == 1:
                valorconv = int(input('Digite o tempo em Semanas: '))
                conv = valorconv * 604800
                print('{} semanas equivalem a {:.2f} segundos'.format(valorconv, conv))
            elif tempo1 == 5 and tempo2 == 2:
                valorconv = int(input('Digite o tempo em Semanas: '))
                conv = valorconv * 10080
                print('{} semanas equivalem a {:.2f} minutos'.format(valorconv, conv))
            elif tempo1 == 5 and tempo2 == 3:
                valorconv = int(input('Digite o tempo em Semanas: '))
                conv = valorconv * 168
                print('{} semanas equivalem a {:.2f} horas'.format(valorconv, conv))
            elif tempo1 == 5 and tempo2 == 4:
                valorconv = int(input('Digite o tempo em Semanas: '))
                conv = valorconv * 7
                print('{} semanas equivalem a {:.2f} dias'.format(valorconv, conv))
            elif tempo1 == 5 and tempo2 == 6:
                valorconv = int(input('Digite o tempo em Semanas: '))
                conv = valorconv / 4.35
                print('{} semanas equivalem a {:.2f} meses'.format(valorconv, conv))
            elif tempo1 == 5 and tempo2 == 7:
                valorconv = int(input('Digite o tempo em Semanas: '))
                conv = valorconv / 52.18
                print('{} semanas equivalem a {:.2f} anos'.format(valorconv, conv))
            elif tempo1 == 5 and tempo2 == 5:
                print('Você não pode converter Semanas em Semanas, escolha outra opção.')

            if tempo1 == 6 and tempo2 == 1:
                valorconv = int(input('Digite o tempo em Meses: '))
                conv = valorconv * 2629800
                print('{} meses equivalem a {:.2f} segundos'.format(valorconv, conv))
            elif tempo1 == 6 and tempo2 == 2:
                valorconv = int(input('Digite o tempo em Meses: '))
                conv = valorconv * 43830
                print('{} meses equivalem a {:.2f} minutos'.format(valorconv, conv))
            elif tempo1 == 6 and tempo2 == 3:
                valorconv = int(input('Digite o tempo em Meses: '))
                conv = valorconv * 730.5
                print('{} meses equivalem a {:.2f} horas'.format(valorconv, conv))
            elif tempo1 == 6 and tempo2 == 4:
                valorconv = int(input('Digite o tempo em Meses: '))
                conv = valorconv * 30.44
                print('{} meses equivalem a {:.2f} dias'.format(valorconv, conv))
            elif tempo1 == 6 and tempo2 == 5:
                valorconv = int(input('Digite o tempo em Meses: '))
                conv = valorconv * 4.35
                print('{} meses equivalem a {:.2f} semanas'.format(valorconv, conv))
            elif tempo1 == 6 and tempo2 == 7:
                valorconv = int(input('Digite o tempo em Meses: '))
                conv = valorconv / 12
                print('{} meses equivalem a {:.2f} anos'.format(valorconv, conv))
            elif tempo1 == 6 and tempo2 == 6:
                print('Você não pode converter Meses em Meses, escolha outra opção.')

            if tempo1 == 7 and tempo2 == 1:
                valorconv = int(input('Digite o tempo em Anos: '))
                conv = valorconv * 31557600
                print('{} anos equivalem a {:.2f} segundos'.format(valorconv, conv))
            elif tempo1 == 7 and tempo2 == 2:
                valorconv = int(input('Digite o tempo em Anos: '))
                conv = valorconv * 525960
                print('{} anos equivalem a {:.2f} minutos'.format(valorconv, conv))
            elif tempo1 == 7 and tempo2 == 3:
                valorconv = int(input('Digite o tempo em Anos: '))
                conv = valorconv * 8766
                print('{} anos equivalem a {:.2f} horas'.format(valorconv, conv))
            elif tempo1 == 7 and tempo2 == 4:
                valorconv = int(input('Digite o tempo em Anos: '))
                conv = valorconv * 365.25
                print('{} anos equivalem a {:.2f} dias'.format(valorconv, conv))
            elif tempo1 == 7 and tempo2 == 5:
                valorconv = int(input('Digite o tempo em Anos: '))
                conv = valorconv * 52.18
                print('{} anos equivalem a {:.2f} semanas'.format(valorconv, conv))
            elif tempo1 == 7 and tempo2 == 6:
                valorconv = int(input('Digite o tempo em Anos: '))
                conv = valorconv * 12
                print('{} anos equivalem a {:.2f} meses'.format(valorconv, conv))
            elif tempo1 == 7 and tempo2 == 7:
                print('Você não pode converter Anos em Anos, escolha outra opção.')

        # Laço para converter Temperatura

        elif escmedida == 4:
            temper1 = int(input('Deseja converter de \n[1] Celsius\n[2] Fahrenheit\n[3] Kelvin\n'))
            temper2 = int(input('Para \n[1] Celsius\n[2] Fahrenheit\n[3] Kelvin\n'))

            if temper1 == 1 and temper2 == 2:
                valorconv = float(input('Digite a temperatura em Celsius: '))
                conv = valorconv * 1.8 + 32
                print('º{}C equivalem a º{:.2f}F'.format(valorconv, conv))
            elif temper1 == 1 and temper2 == 3:
                valorconv = float(input('Digite a temperatura em Celsius: '))
                conv = valorconv + 273.15
                print('º{}C equivalem a {:.2f}K'.format(valorconv, conv))
            elif temper1 == 1 and temper2 == 1:
                print('Você não pode converter Celsius em Celsius, escolha outra opção.')

            if temper1 == 2 and temper2 == 1:
                valorconv = float(input('Digite a temperatura em Fahrenheit: '))
                conv = (valorconv - 32) / 1.8
                print('º{}F equivalem a º{:.2f}C'.format(valorconv, conv))
            elif temper1 == 2 and temper2 == 3:
                valorconv = float(input('Digite a temperatura em Fahrenheit: '))
                conv = (valorconv + 459.67) / 1.8
                print('º{}F equivalem a {:.2f}K'.format(valorconv, conv))
            elif temper1 == 2 and temper2 == 2:
                print('Você não pode converter Fahrenheit em Fahrenheit, escolha outra opção.')

            if temper1 == 3 and temper2 == 1:
                valorconv = float(input('Digite a temperatura em Kelvin: '))
                conv = valorconv - 273.15
                print('{}K equivalem a º{:.2f}C'.format(valorconv, conv))
            elif temper1 == 3 and temper2 == 2:
                valorconv = float(input('Digite a temperatura em Kelvin: '))
                conv = valorconv * 1.8 - 459.67
                print('{}K equivalem a º{:.2f}F'.format(valorconv, conv))
            elif temper1 == 3 and temper2 == 3:
                print('Você não pode converter Kelvin em kelvin, escolha outra opção.')

        num = int(input('\nDigite 0 para voltar'))

print('Obrigado por utilizar, {}!'.format(nome))
