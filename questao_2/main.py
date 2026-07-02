def calcular_total_vagas(vagas):
    return len(vagas)


def calcular_vagas_ocupadas(vagas):
    contador = 0
    for numero, tipo, ocupada in vagas:
        if ocupada:
            contador += 1
    return contador


def calcular_vagas_livres(vagas):
    contador = 0
    for numero, tipo, ocupada in vagas:
        if not ocupada:
            contador += 1
    return contador


def calcular_livres_por_categoria(vagas):
    comum = 0
    idoso = 0
    pcd = 0
    for numero, tipo, ocupada in vagas:
        if not ocupada:
            if tipo == "comum":
                comum += 1
            elif tipo == "idoso":
                idoso += 1
            elif tipo == "pcd":
                pcd += 1
    return comum, idoso, pcd


def status_estacionamento(livres):
    if livres == 0:
        return "LOTADO"
    elif livres <= 2:
        return "QUASE LOTADO"
    else:
        return "DISPONÍVEL"


def buscar_vaga(vagas, numero_buscado):
    descricao = {"comum": "vagas comuns", "idoso": "idosos", "pcd": "PCD"}
    for numero, tipo, ocupada in vagas:
        if numero == numero_buscado:
            situacao = "ocupada" if ocupada else "livre"
            print(f"A vaga {numero} é destinada a {descricao.get(tipo, tipo)} e está {situacao}.")
            return
    print("Vaga não encontrada.")


vagas = [
    (1, "comum", True),
    (2, "idoso", False),
    (3, "pcd", False),
    (4, "comum", True),
    (5, "comum", False)
]

total = calcular_total_vagas(vagas)
ocupadas = calcular_vagas_ocupadas(vagas)
livres = calcular_vagas_livres(vagas)
comum, idoso, pcd = calcular_livres_por_categoria(vagas)
status = status_estacionamento(livres)

print("===== ESTACIONAMENTO SHOPPING CENTRAL =====")
print(f"Total de vagas: {total}")
print(f"Vagas ocupadas: {ocupadas}")
print(f"Vagas livres: {livres}")
print(f"Vagas comuns livres: {comum}")
print(f"Vagas para idosos livres: {idoso}")
print(f"Vagas PCD livres: {pcd}")
print(f"Status do estacionamento: {status}")

numero_vaga = int(input("Digite o número da vaga: "))
buscar_vaga(vagas, numero_vaga)
