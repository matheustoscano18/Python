def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicioar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    alunos = dict()
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['menor'] = min(n)
    alunos['média'] = sum(n) / len(n)
    if sit:
        if alunos['média'] >= 7:
            alunos['situação'] = 'BOA'
        elif 5 <= alunos['média'] < 7:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    return alunos


# Programa Principal
print("-" * 30)
resp = notas(5.5, 2.5, 10, 9.3, sit=True)
print(resp)
