# -*- coding: utf-8 -*-

# python main.py < testInput.txt > testOutput.txt

interation = int(input())

for _ in range(interation):
    row = input()
    A,B = row.split(' ')[0][::-1] , row.split(' ')[1][::-1] #separa e inverte as strings 

    if len(B) > len(A):
        print('nao encaixa')
        continue
    desc = 1

    for i in enumerate(B):
        if i[1] != A[i[0]]:
            print('nao encaixa')
            desc = 0
            break
    if desc:
        print('encaixa')
    
