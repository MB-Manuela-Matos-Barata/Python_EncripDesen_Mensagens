# utils.py

from matriz import matriz_carateres, matriz_numeros

def encriptar(mensagem):
    mensagem = mensagem.upper()
    mensagem_encriptada = ""

    for letra in mensagem:
        encontrado = False
        for i in range(len(matriz_carateres)):
            for j in range(len(matriz_carateres[i])):
                if matriz_carateres[i][j] == letra:
                    mensagem_encriptada += matriz_numeros[i][j]
                    encontrado = True
                    break
            if encontrado:
                break
        if not encontrado:
            mensagem_encriptada += "??"  # símbolo não reconhecido
    return mensagem_encriptada


def desencriptar(mensagem):
    mensagem_desencriptada = ""
    for i in range(0, len(mensagem), 2):
        codigo = mensagem[i:i+2]
        encontrado = False
        for x in range(len(matriz_numeros)):
            for y in range(len(matriz_numeros[x])):
                if matriz_numeros[x][y] == codigo:
                    mensagem_desencriptada += matriz_carateres[x][y]
                    encontrado = True
                    break
            if encontrado:
                break
        if not encontrado:
            mensagem_desencriptada += "?"
    return mensagem_desencriptada
