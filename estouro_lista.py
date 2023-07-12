def verificar_tamanho_lista(lista, tamanho_maximo):
    if len(lista) > tamanho_maximo:
        raise ValueError("Tamanho máximo da lista excedido!")

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
tamanho_maximo = 3

try:
    verificar_tamanho_lista(lista, tamanho_maximo)
except ValueError as e:
    print(f"Erro: {e}")
