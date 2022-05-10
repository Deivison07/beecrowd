# -*- coding: utf-8 -*-

while True:
    try:

        row = input().split(' ')
        Hashmat = int(row[0])
        outro = int(row[1])
        print(f'{abs(Hashmat-outro)} ')
    

    except Exception:
        break