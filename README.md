# Sistema de Cálculo de Médias

Projeto feito durante as aulas de Python na FIAP.

A ideia surgiu de um exercício em aula: coletar uma quantidade variável de notas via `input()` e calcular a média automaticamente. Depois adaptei para uma página web.

## O que aprendi

- Usar `*args` para receber qualquer quantidade de argumentos numa função
- Passar uma lista como argumentos com `*lista`
- Coletar dados do usuário com `input()` dentro de um `for`
- Verificar situação do aluno com `if/elif/else`

## Versão Python (terminal)

```python
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
```

## Como rodar

```bash
python medias.py
```

Ou abra o `index.html` no navegador para a versão web.

---
Feito por Igor Davi · FIAP Engenharia de Software
