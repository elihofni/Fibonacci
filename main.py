import sys
import time

SEQUENCIA = [1, 1, 2]


def recursivo(numero=0):
    if numero < 2:
        return numero
    valor = recursivo(numero - 1) + recursivo(numero - 2)
    return valor


def iterativo(numero=0):
    if numero > 2:
        for i in range(3, numero, 1):
            SEQUENCIA.append(SEQUENCIA[i - 1] + SEQUENCIA[i - 2])
    return SEQUENCIA


if __name__ == '__main__':
    METODOS = {
        '-r': {'func': recursivo, 'nome': 'Recursivo'},
        '-i': {'func': iterativo, 'nome': 'Iterativo'},
    }

    _, *inputs = sys.argv

    numero = int(inputs[0]) if bool(inputs) else 0
    metodo = inputs[1] if len(inputs) == 2 else '-i'

    funcao = METODOS[metodo]['func']
    nome = METODOS[metodo]['nome']
    inicio_cronometro = time.time()
    sequencia = funcao(numero)
    fim_cronometro = time.time()
    tempo_decorrido = (fim_cronometro - inicio_cronometro) * 1000.0

    print('\nFIBONACCI - %s\n' % nome)
    if metodo == '-r':
        print(sequencia)
    else:
        print(SEQUENCIA)
    print('\nLevou {:.3f}ms'.format(tempo_decorrido))
