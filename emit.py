from os import path, remove
from threading import Lock

lock = Lock()

def deletar_intermediario(intermediario):
    if path.exists(intermediario):
        remove(intermediario)


def emitir_intermediario(chave, ocorrencia):
    """Escreve em um arquivo intermediario um valor chave 
    seguido de sua acorrencia

    Args:
        chave (string): Nome da chave
        ocorrencia (char): o total de ocorrencias
    """
    intermediario = "./intermediario"
    if not path.exists(intermediario):
        open(intermediario, 'w').close()

    lock.acquire()
    with open(intermediario, "a") as arquivo:
        arquivo.write("{} {}\n".format(chave, ocorrencia))
    lock.release()


def ler_intermediario(intermediario):
    dic_palavras = {}
    with open(intermediario, 'r') as arquivo:
        for line in arquivo.readlines():
            chave, valor = line.strip().split()
            if dic_palavras.get(chave) is not None:
                dic_palavras[chave].append(valor)
            else:
                dic_palavras[chave] = [valor]
    return dic_palavras


def deletar_final(final):
    if path.exists(final):
        remove(final)


def emitir_final(chave, ocorrencias):
    final = './final'
    lock.acquire()
    if not path.exists(final):
        open(final, 'w').close()

    with open(final, 'a') as arquivo:
        arquivo.write("{} {}\n".format(chave, ocorrencias))
    lock.release()