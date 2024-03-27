from concurrent.futures import ThreadPoolExecutor
from os import listdir

from MapReduce import Map
from emit import deletar_intermediario


if __name__ == "__main__":

    deletar_intermediario('./intermediario')


    arquivos = './arquivos'
    quantidade_arquivos = len(listdir(arquivos))


    with ThreadPoolExecutor(max_workers=10) as executor:
        for index in range(quantidade_arquivos):
            executor.submit(Map, f"arquivo{index}.txt", "foo")
