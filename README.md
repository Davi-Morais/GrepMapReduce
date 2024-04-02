Equipe: 
- Davi de Morais Farias
- Jose Igor Venancio de Albuquerque

# Grep MapReduce: buscar padroes de palavras

Instruções:

Para buscar em quantas linhas uma determinada palavra aparece, execute o arquivo como nos exemplos:
```python
python3 grep.py  "bed"
```
```python
python3 grep.py "fffff"
```
```python
python3 grep.py "abcde"
```

Para procurar padroes usando expressões regulares, use a opcao **-e**, como nos exemplos:

Letras minúsculas sequenciais:
```python
python3 grep.py -e "[a-z]{4}"
```

Buscar emails:
```python
python3 grep.py -e "[\w\-.]+@[\w\-]+\.\w+\.?\w*"
```
Buscar cpf:
```python
python3 grep.py -e "([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"
```