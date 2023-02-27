'''Programa que tenha função notas()
- receber várias notas de alunos
- retornar um dicionario com as seguintes info:
    - quantidade de notas
    - a maior nota
    - a menor nota
    - a média da turma
    - a situação (opcional)'''
def notas(*num, show=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param show: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {}
    dados['Total'] = len(num)
    dados['Maior'] = max(num)
    dados['Menor'] = min(num)
    dados['Média'] = sum(num)/len(num)
    if show:
        if dados['Média'] >= 7:
            dados['Situação'] = 'Boa'
        elif dados['Média'] >= 5:
            dados['Situação'] = 'Razoável'
        else:
            dados['Situação'] = 'Ruim'
    return dados


resp = notas(9.5, 5.5, 2.5, 8.5, show=True)
print(resp)
help(notas
     
