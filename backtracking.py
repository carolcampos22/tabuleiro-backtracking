tabuleiro = [[" ", " ", " "], [" ", " ", "x"], ["x", " ", " "], [" ", " ", " "]]

direcoes = [
    [0, 1],
    [0, -1],
    [ -1, 0],
    [1, 0],
]  # (direita, esquerda, cima, baixo)


def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|" + "|".join(linha) + "|")

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    melhor_profundidade = float("inf")
    melhor_linha = linha_atual
    melhor_coluna = coluna_atual

    for direcao in direcoes:
        delta_linha, delta_coluna = direcao
        nova_linha = linha_atual + delta_linha
        nova_coluna = coluna_atual + delta_coluna

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            if chegou_destino(nova_linha, nova_coluna):
                return nova_linha, nova_coluna, profundidade

            tabuleiro[nova_linha][nova_coluna] = "*"

            linha_final, coluna_final, nova_profundidade = proximo_movimento(
                tabuleiro, nova_linha, nova_coluna, profundidade + 1
            )

            tabuleiro[nova_linha][nova_coluna] = " "

            if nova_profundidade < melhor_profundidade:
                melhor_profundidade = nova_profundidade
                melhor_linha = linha_final
                melhor_coluna = coluna_final

    return melhor_linha, melhor_coluna, melhor_profundidade



def movimento_valido(tabuleiro, linha, coluna):
    return ( 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]) and tabuleiro[linha][coluna] == " ")
    


def chegou_destino(linha, coluna):
    return linha == 0 and coluna == 2
    

def main():
    linha_atual = 3
    coluna_atual = 0
    tabuleiro[linha_atual][coluna_atual] = "*"

    print("Tabueiro inicial: ")
    mostrar_tabuleiro(tabuleiro)

    while not chegou_destino(linha_atual, coluna_atual):
       nova_linha, nova_coluna, profundidade =  proximo_movimento(tabuleiro, linha_atual, coluna_atual, 1)

       if profundidade == float("inf"):
           print("Não foi possível encontrar um caminho até o destino.")
           return
       
       linha_atual = nova_linha
       coluna_atual = nova_coluna
       tabuleiro[linha_atual][coluna_atual] = "*"

       print("\n Tabuleiro atualizado:")
       mostrar_tabuleiro(tabuleiro)
    
    print("\n Chegou ao destino!")

if __name__ == "__main__":
    main()



