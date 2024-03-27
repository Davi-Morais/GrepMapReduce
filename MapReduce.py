from re import search

from emit import emitir_intermediario, emitir_final

def Map(key, padrao):
    with open(f"./arquivos/{key}", 'r') as arquivo:
        for line in arquivo.readlines():
            if (search(padrao, line)):
                emitir_intermediario(key, line.strip())


def Reduce(chave, lista_ocorrencia):
    emitir_final(chave, len(lista_ocorrencia))
