from concurrent.futures import ThreadPoolExecutor

from MapReduce import Reduce
from emit import deletar_final, ler_intermediario


if __name__ == "__main__":

    deletar_final('./final')

    intermadiario = './intermediario'

    dicionario = ler_intermediario(intermadiario)

    # Maximo de 10 threads:
    with ThreadPoolExecutor(max_workers=10) as executor: 
        for key in sorted(dicionario.keys()):
            executor.submit(Reduce, key, dicionario[key])