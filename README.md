Equipe: 
- Davi de Morais Farias
- Jose Igor Venancio de Albuquerque

# Grep MapReduce: buscar padroes de palavras

Instruções:

Para buscar em quantas linhas uma determinada palavra aparece, execute o arquivo como nos exemplos:
```python
python3 grep.py "ads"
```
```python
python3 grep.py "foo"
```
```python
python3 grep.py "asdf"
```

Para procurar padroes usando expressões regulares, use a opcao **-e**, como nos exemplos:

```python
python3 grep.py -e "foo$"
```
```python
python3 grep.py -e "[a-z]{4}"
```

Buscar emails:
```python
python3 grep.py -e "^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})$"
```