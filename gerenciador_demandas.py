demandas = []

def cadastrar_demanda(id_demanda, titulo, solicitante, prioridade, cep="", cidade=""):
    if not titulo.strip() or not solicitante.strip():
        print("Campos obrigatórios vazios!")
        return

    for d in demandas:
        if d["id"] == id_demanda:
            print("ID já cadastrado!")
            return

    demandas.append({
        "id": id_demanda,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "status": "Aberta"
    })
    print("Cadastrado com sucesso!")


def listar_demandas():
    if not demandas:
        print("Nenhuma demanda cadastrada!")
        return
    for d in demandas:
        print(d)


def buscar_demanda(termo):
    for d in demandas:
        if d["id"] == termo or termo.lower() in d["titulo"].lower():
            print(d)
            return d
    print("Não encontrada!")


def atualizar_status(id_demanda, novo_status):
    for d in demandas:
        if d["id"] == id_demanda:
            d["status"] = novo_status
            print("Status atualizado!")
            return
    print("Não encontrada!")


def excluir_demanda(id_demanda):
    for d in demandas:
        if d["id"] == id_demanda:
            demandas.remove(d)
            print("Demanda excluída!")
            return
    print("Não encontrada!")

#TESTE**
if __name__ == "__main__":
    cadastrar_demanda(1, "Ajuste de rede", "Carlos", "ALTA", "55150000", "Belo Jardim")
    listar_demandas()
    buscar_demanda(1)
    atualizar_status(1, "Concluída")
    excluir_demanda(1)