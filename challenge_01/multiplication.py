# Escreva um programa em Python que leia um número inteiro e gere a
# tabuada do número lido entre 1 a 10.


def tabuada(num):
    result = [num * i for i in range(1, 11)]
    print(result)
    return result


if __name__ == "__main__":
    num = int(input("Digite um número: "))
    tabuada(num)
