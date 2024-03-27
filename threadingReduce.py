import logging
import threading
from concurrent.futures import ThreadPoolExecutor

from MapReduce import Reduce
from emit import deletar_final, ler_intermediario


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    deletar_final('./final')

    intermadiario = './intermediario'

    dicionario_palavras = ler_intermediario(intermadiario)
   

    # threads = list()
    # for key, ocorrencia in dicionario_palavras.items():
    #     x = threading.Thread(target=Reduce, args=(key, ocorrencia,))
    #     threads.append(x)
    #     x.start()
        
    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index)
    #     thread.join()
    #     logging.info("Main    : thread %d done", index)


    # # Maximo de 10 threads:
    with ThreadPoolExecutor(max_workers=10) as executor: 
        for key, ocorrencia in dicionario_palavras.items():
            executor.submit(Reduce, key, ocorrencia)