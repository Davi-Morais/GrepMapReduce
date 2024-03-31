from re import search
from threading import Lock

from emit import emitir_intermediario, emitir_final

lock = Lock()

def Map(key, padrao):
    with open(f"./arquivos/{key}", 'r') as arquivo:
        for line in arquivo.readlines():
            if padrao in line:
                emitir_intermediario(key, line.strip())


def Reduce(chave, ocorrencia):
    lock.acquire()
    for frase in ocorrencia:
        emitir_final(chave, frase)
    lock.release()
