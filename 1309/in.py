s = 'a'

suf = s

index = (len(suf))
total = 0

while index > 0:
    for i in enumerate(suf):
        try:
            if s[i[0]] == suf[i[0]]:
                print(f'{s[i[0]]} é igual  {suf[i[0]]}')
                total+=1
            else:
                break
        except:
            pass
        
    print(f'----------------{suf , total ,s}')
    suf = suf[1:]
    
        
    index-=1

print(total)