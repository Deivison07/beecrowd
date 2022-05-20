
while True:
    try:
        row = input()
        esquerdo = 0
        direito = 0

        for i in row:
            if i == '(':
                esquerdo+=1
            elif i == ')':
                direito+=1
            
            if direito > esquerdo:
                print('incorrect')
                break
        
        if esquerdo-direito:
            print('incorrect')
        else:
            print('correct')
    except:
        break