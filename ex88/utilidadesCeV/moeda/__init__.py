def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Função que aumenta um valor em n%
    :param preco: valor bruto inserido pelo usuário
    :param taxa: taxa de aumento do valor
    :param formato: formatação do valor
    :return: opção de formatar ou não o valor, basta mudar de False para True
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """
       -> Função que aumenta um valor em n%
       :param preco: valor bruto inserido pelo usuário
       :param taxa: taxa de diminuição do valor
       :param formato: formatação do valor
       :return: opção de formatar ou não o valor, basta mudar de False para True
       """
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    """
    -> Função que dobra o valor de n
    :param preco: valor bruto inserido pelo usuário
    :param formato: formatação do valor
    :return: opção de formatar ou não o valor, basta mudar de False para True
    """
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    """
        -> Função que retorna metade do valor de n
        :param preco: valor bruto inserido pelo usuário
        :param formato: formatação do valor
        :return: opção de formatar ou não o valor, basta mudar de False para True
        """
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> É a função que formata todos os valores
    :param preco: valor bruto inserido pelo usuário
    :param moeda: insere a sigla da moeda de sua preferência
    :return: Retornará os valores formatados substituindo o "." pela ","
    """
    return f"{moeda}{preco:>.2f}".replace('.', ',')


def resumo(preco=0, taxamais=0, taxadim=0):
    """Todas as funcionalidades em uma só função"""
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: {moeda(preco):>12}")
    print(f"Dobro do preço: {dobro(preco, True):>13}")
    print(f"Metade do preço: {metade(preco, True):>11}")
    print(f"{taxamais}% de aumento: {aumentar(preco, taxamais, True):>13}")
    print(f"{taxadim}% de redução: {diminuir(preco, taxadim, True):>12}")
    print("-" * 30)
