import argparse
from sys import exit
from concurrent.futures import ThreadPoolExecutor
from os import listdir

from MapReduce import Map, Reduce
from emit import deletar_intermediario, deletar_final, ler_intermediario



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog='Grep MapReduce',
                    description='Procura padroes de texto e gera um arquivo final com as ocorrencias',
                    epilog='MapReduce Sistemas Distribuidos 2024')
    parser.add_argument('padrao', nargs='?', help="Texto que vai ser buscado.")
    parser.add_argument('-e', help="Recebe uma expressao regular.")

    args = parser.parse_args()
    
    padrao_busca = None
    if args.padrao:
        padrao_busca = args.padrao
    elif args.e:
        padrao_busca = args.e
    else:
        print("Nenhum padrao informado...")
        exit(1)

    intermadiario = './intermediario'
    final = './final'

    deletar_intermediario(intermadiario)
    deletar_final(final)


    arquivos = './arquivos'
    quantidade_arquivos = len(listdir(arquivos))


    # Maximo de 10 threads:
    with ThreadPoolExecutor(max_workers=10) as executor:
        for index in range(quantidade_arquivos):
            executor.submit(Map, f"arquivo{index}.txt", padrao_busca)



    dicionario = ler_intermediario(intermadiario)
    # Maximo de 10 threads:
    with ThreadPoolExecutor(max_workers=10) as executor: 
        for key in sorted(dicionario.keys()):
            executor.submit(Reduce, key, dicionario[key])