expr = str(input('Digite a expressãg: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append("(")
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está encada!')