from concurrent.futures import ThreadPoolExecutor
from os import listdir

from MapReduce import Map, Reduce
from emit import deletar_intermediario, deletar_final, ler_intermediario



if __name__ == "__main__":

    intermadiario = './intermediario'
    final = './final'

    deletar_intermediario(intermadiario)
    deletar_final(final)


    arquivos = './arquivos'
    quantidade_arquivos = len(listdir(arquivos))


    # Maximo de 10 threads:
    with ThreadPoolExecutor(max_workers=10) as executor:
        for index in range(quantidade_arquivos):
            executor.submit(Map, f"arquivo{index}.txt", "foo")



    dicionario = ler_intermediario(intermadiario)
    # Maximo de 10 threads:
    with ThreadPoolExecutor(max_workers=10) as executor: 
        for key in sorted(dicionario.keys()):
            executor.submit(Reduce, key, dicionario[key])