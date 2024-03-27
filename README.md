Equipe: 
- Davi de Morais Farias
- Jose Igor Venancio de Albuquerque

# Map Reduce: contar ocorrência de palavras

Instruções:

1. Execute o arquivo ***file_generator.py*** para criar alguns arquivos com palavras aleatórias
2. Execute o arquivo ***threadingMap.py*** para ler cada arquivo criado no passo anterior, e gerar um arquivo ***intermediario*** com todas essas palavras e sua ocorrência. Uma thread para ler cada arquivo
3. Execute o arquivo ***threadingReduce.py*** para ler o arquivo ***intermediario***, contar quantas vezes uma mesma palavra apareceu, e escrever em um arquivo ***final*** essas ocorrências. Uma thread para cada palavra que pode ou não ter se repetido.