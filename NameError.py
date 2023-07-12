try:
    # Bloco de código com erro
    print("variavel_inexistente")
except NameError as e:
    # Tratamento da exceção
    print(f"Erro: {e}")