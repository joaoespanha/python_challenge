# Escreva um programa em python que leia uma palavra, verifique se
# a palavra começa por letra maiúscula ou minúscula.
# Informe quantas letras a palavra têm ao total. Informe quantas consoantes a palavra
# têm, bem como as vogais.
# A saída deve informar separadamente cada um dos itens pedidos.


def conta_letras(palavra):
    vogais = 0
    consoantes = 0
    verifica_maiuscula = ""
    quantidade_de_letras = len(palavra)

    if palavra[0].isupper():
        verifica_maiuscula = "maiuscula"
    else:
        verifica_maiuscula = "minuscula"

    for letra in palavra:
        if letra in "aeiou":
            vogais += 1
        else:
            consoantes += 1
    print(
        f"A palavra {palavra} tem {quantidade_de_letras} letras sendo {consoantes} consoantes, {vogais} e começa com letra {verifica_maiuscula}."
    )
    return vogais, consoantes, verifica_maiuscula, quantidade_de_letras
