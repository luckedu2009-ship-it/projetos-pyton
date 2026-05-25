#Ferramenta de Conversao Dolar x Real --
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor Dolar x Real")
preco = float(input("Digite o Preço do produto em dolar: "))
resultado = converter(preco)
print(F"O valor em Reais é:{resultado:.2f}")