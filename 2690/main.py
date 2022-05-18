
interations = int(input())

for _ in range(interations):

    row = input().replace(' ','')

    for i in row:
        if i in 'GQakl':
            row = row.replace(i,'0')

        if i in 'ISblv':
            row = row.replace(i,'1')

        if i in 'EOYcmw':
            row = row.replace(i,'2')

        if i in 'FPZdnx':
            row = row.replace(i,'3')

        if i in 'JTeoy':
            row = row.replace(i,'4')

        if i in 'DNXfpz':
            row = row.replace(i,'5')
        
        if i in 'AKUgq':
            row = row.replace(i,'6')
        
        if i in 'CMWhr':
            row = row.replace(i,'7')

        if i in 'BLVis':
            row = row.replace(i,'8')
        
        if i in 'HRjt':
            row = row.replace(i,'9')

    print(row)
    





