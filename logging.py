import logging

# Configurar o logging para salvar as saídas em um arquivo
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# Exemplo de linha de código para debug
numero = 42
logging.debug(f'O valor do número é {numero}')
