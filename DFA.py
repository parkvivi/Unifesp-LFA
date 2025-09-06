# Implementar um programa que calcule a função de transição estendida de um DFA. 
# A entrada do programa é um DFA e uma string. O programa diz se a string 
# pertence ou não à linguagem definida pelo DFA.

def DefineDFA() -> tuple[int, list[str], list[list[int]], int, list[int]]:
    print("Quantidade de estados: ", end='')
    NumEst: int = int(input())

    print("Estado inicial: ", end='')
    EstInicial: int = int(input())

    print("Estado(s) final(is): ", end='')
    StringEstFinal: str = input()

    EstFinal: list[int] = []
    for estado in StringEstFinal.split(" "):
        EstFinal.append(int(estado))

    print("Alfabeto: ", end='')
    StringAlfabeto: str = input()

    Alfabeto: list[str] = StringAlfabeto.split(" ")

    FuncaoTransicao: list = []

    for estado in range(NumEst):
        FuncaoTransicao.append([])
        for simbolo in Alfabeto:
            print(f"d({estado}, {simbolo}) = ", end='')
            FuncaoTransicao[estado].append(int(input()))

    return [NumEst, Alfabeto, FuncaoTransicao, EstInicial, EstFinal]

def FuncaoTransicaoEstendida(dfa: tuple, string: str):
    NumEst, Alfabeto, FuncaoTransicao, EstInicial, EstFinal = dfa
    print(f"d({EstInicial}, null) = {EstInicial}")
    EstAnterior: int = EstInicial

    for i, simbolo in enumerate(string):
        if simbolo not in Alfabeto:
            print("String não aceita")
            return
        ProxEstado: int = FuncaoTransicao[EstAnterior][Alfabeto.index(simbolo)]
        print(f"d({EstAnterior}, {string[0:i+1]}) = {ProxEstado}")
        EstAnterior = ProxEstado

    if EstAnterior not in EstFinal:
        print("String não aceita")
    else:
        print("String aceita")

def main():
    dfa: tuple = DefineDFA()

    print("Digite uma string: ", end='')
    string: str = input()

    FuncaoTransicaoEstendida(dfa, string)

if __name__ == "__main__":
    main()