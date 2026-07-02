# Questão 4 — Triagem de atendimento em unidade de saúde

# Uma unidade de saúde precisa organizar a ordem de prioridade dos pacientes que chegam para atendimento.

# Cada paciente será representado por uma tupla:

# (nome, idade, temperatura, possui_doenca_cronica)

# Exemplo:

# pacientes = [

#     ("Ana", 29, 37.2, False),

#     ("Carlos", 68, 38.5, True),

#     ("Mariana", 42, 39.1, False),

#     ("João", 15, 36.7, False)

# ]

# A equipe deverá criar uma classificação de prioridade para cada paciente.

# Regras de prioridade

# Um paciente será classificado como:

# Prioridade alta

# temperatura maior ou igual a 39°C;
# idade maior ou igual a 60 anos e febre maior ou igual a 38°C;
# possui doença crônica e temperatura maior ou igual a 38°C.

# Prioridade média

# temperatura entre 37.8°C e 38.9°C;
# idade menor que 12 anos ou maior que 60 anos.

# Prioridade baixa

# demais casos.
# O programa deverá

# Criar uma função para classificar a prioridade de um paciente.
# Criar uma função para contar quantos pacientes existem em cada nível de prioridade.
# Exibir a lista de pacientes com sua classificação.
# Criar três listas:

# pacientes de prioridade alta;
# pacientes de prioridade média;
# pacientes de prioridade baixa.
# Informar qual grupo deve ser atendido primeiro.
# Uso obrigatório

# lista de tuplas como entrada;
# criação e manipulação de listas;
# funções;
# laço de repetição;
# condicionais compostas;
# uso adequado de operadores lógicos and e or.
# Exemplo de saída

# ===== TRIAGEM DE PACIENTES =====

# Ana - Prioridade baixa

# Carlos - Prioridade alta

# Mariana - Prioridade alta

# João - Prioridade média

# Resumo:

# Prioridade alta: 2 pacientes

# Prioridade média: 1 paciente

# Prioridade baixa: 1 paciente

# O próximo grupo a ser atendido é: PRIORIDADE ALTA


pacientes = []
prioridade_alta = []
prioridade_media = []
prioridade_baixa = []
contagem_paciente = 0

def cadastra_paciente(nome: str, idade: int, temperatura: float, possui_doenca_cronica: bool):
    pacientes.append((nome, idade, temperatura, possui_doenca_cronica))


def classifica_prioridade(contagem_paciente: int, pacientes: list):
    global prioridade_alta
    global prioridade_media
    global prioridade_baixa
    paciente = pacientes[contagem_paciente]
    if paciente[2] > 39:
        prioridade_alta.append((paciente[0], 'Prioridade Alta'))
    if paciente[1] >= 60 and paciente[2] >= 38:
        prioridade_alta.append((paciente[0], 'Prioridade Alta'))
    if paciente[3] == True and paciente[2] >= 38:
        prioridade_alta.append((paciente[0], 'Prioridade Alta'))
    if paciente[1] < 12 or paciente[1] > 60:
        prioridade_media.append((paciente[0], 'Prioridade Média'))
    if paciente[2] >= 37.8 and paciente[2] <= 38.9:
        prioridade_media.append((paciente[0], 'Prioridade Média'))
    prioridade_baixa.append((paciente[0], 'Prioridade Baixa'))
    

def interface_menu():
    print('\033c', end='')
    input ('Selecione a tarefa desejada: '
           '1 - Triagem de Pacientes; '
           '2 - Ver Pacientes em Atendimento por Prioridade'
           '3 - ')


def triagem():
    print('\033c', end='')
    global contagem_paciente
    global pacientes
    while True:
        print('\n'
                '===== TRIAGEM DE PACIENTES ====='
                '\n')
        while True:
            nome = input('Digite o nome do paciente: ')
            if nome in '1234567890':
                input('Erro! Digite somente caracteres alfanuméricos.')
                print('\033c', end='')
            idade = int(input('Idade: '))
            if idade < 0:
                input('Erro! Digite um número inteiro positivo.')
                print('\033c', end='')
            else:
                break
        while True:
            temperatura = float(input('Digite a temperatura: '))
            break
        while True:
            doenca_cronica = input('Possui doença cronica? [s/n] ')
            if doenca_cronica == 's':
                possui_doenca_cronica = True
                break
            if doenca_cronica == 'n':
                possui_doenca_cronica = False
                break
        cadastra_paciente(nome, idade, temperatura, possui_doenca_cronica)
        contagem_paciente = len(pacientes)
        classifica_prioridade(contagem_paciente, pacientes)
        break


interface_menu()
