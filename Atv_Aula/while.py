ini = int(input('Digite o início: '))
end = int(input('Digite o final: '))

if ini < end:
    while ini <= end:
        print(f'n: {ini}')
        ini += 1

elif ini > end:
    while ini >= end:
        print(f'n: {ini}')
        ini -= 1

else:
    print(f'n: {ini}')
