
interations = int(input())

for x in range(interations):
    soma = 0

    linha = input().split(' ')

    PA = int(linha[0])
    PB = int(linha[1])
    G1 = float(linha[2])
    G2 = float(linha[3])

    while True:
        if PA > PB:
            if soma > 100:
                print('Mais de 1 seculo.')
                break

            print(f'{soma} anos.')
            break
        else:
            soma+=1

            PA = (PA + (PA*(G1/100)))//1

            PB = (PB + (PB*(G2/100)))//1









