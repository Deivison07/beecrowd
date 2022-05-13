import locale
locale.setlocale(locale.LC_MONETARY, ('en_US.UTF-8'))

while True:
    try:
        
        dolares = int(input())
        centavos = int(input())/100

        dolares += centavos

        valor = locale.currency(dolares, grouping=True)
        print(valor)
    except:
        break




