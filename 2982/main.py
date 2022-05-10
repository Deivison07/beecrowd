# -*- coding: utf-8 -*-
#python main.py < testInput.txt > testOutput.txt

interation = int(input())

soma = 0
for _ in range(interation):
    row = input().split(' ')
    if row[0] == 'G':
        soma = soma + ( int(row[1])*-1)
    else:
        soma = soma + int(row[1])

if soma < 0:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
else:
    print('A greve vai parar.')

