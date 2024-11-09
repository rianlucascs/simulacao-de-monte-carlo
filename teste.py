codigo = """
def saudacao(nome):
 return f"Olá, {nome}!"
"""

exec(codigo)  # Executa o código que define a função

print(saudacao("João"))  # Saída: Olá, João!