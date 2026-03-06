def media(*args):
    s = 0
    for i in args:
        s += i
    return s / len(args)


l = []
qtde = int(input('Digite a quantidade de notas: '))

for i in range(qtde):
    l.append(float(input(f'Digite a nota {i+1}: ')))

print('Notas:', l)
print('Média:', media(*l))

if media(*l) >= 7:
    print('Situação: Aprovado')
elif media(*l) >= 5:
    print('Situação: Recuperação')
else:
    print('Situação: Reprovado')
