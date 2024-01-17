from challenge import conta_letras


def test_conta_letras():
    assert conta_letras("python") == (1, 5, "minuscula", 6)
    assert conta_letras("Pge") == (1, 2, "maiuscula", 3)
