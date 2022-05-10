
while True:
    row = input().split(' ')
    if row[0] == '0' and row[1] == '0':
        break
    
    carrySoma = 0
    carry = 0
    
    x = row[0][::-1]
    y = row[1][::-1]

    if len(x)>len(y):
        for index in range(len(x)-len(y)):
            y+='0'
    else:
        for index in range(len(y)-len(x)):
            x+='0'

    for i in range(len(x)):

        if (int(x[i]) + int(y[i]) + carry) >= 10:
            carrySoma+=1
            carry = 1
        else:
            carry = 0



    if carrySoma > 1:
        print(f'{carrySoma} carry operations.')
    if carrySoma == 1:
        print(f'{carrySoma} carry operation.')
    if carrySoma == 0:
        print('No carry operation.')
