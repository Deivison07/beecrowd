while True:
    try:
        numero = input()
        print(numero)
        if numero == '' or numero ==  ' ': 
            print('error')
            
        if 'O' in numero or 'o' in numero:
            numero = numero.replace('o','0')
            numero = numero.replace('O','0')
        if 'l' in numero:
            numero = numero.replace('l','1')
        if ' ' in numero:
            numero = numero.replace(' ','')
        if ',' in numero:
            numero = numero.replace(',','')
        
        print(numero)
    except:
        break
