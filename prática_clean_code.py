PRAZO_ALTA = 2
PRAZO_MEDIA = 5
PRAZO_BAIXA = 10
REDUCAO_URGENTE = 1


def calcular_prioridade_chamados(chamados):
    chamados_calculados = []

    for chamado in chamados:
        titulo = chamado[0]
        nivel_prioridade = chamado[1]
        urgente = chamado[2]

        if nivel_prioridade == 1:
            prioridade = "ALTA"
            prazo = PRAZO_ALTA
        elif nivel_prioridade == 2:
            prioridade = "MEDIA"
            prazo = PRAZO_MEDIA
        else:
            prioridade = "BAIXA"
            prazo = PRAZO_BAIXA

        if urgente == True:
            prazo = prazo - REDUCAO_URGENTE

        chamados_calculados.append([titulo, prioridade, prazo])

    return chamados_calculados


dados = [
    ["Erro Servidor", 1, True],
    ["Troca Mouse", 3, False],
]

print(calcular_prioridade_chamados(dados))