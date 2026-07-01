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


def cadastra_paciente(nome, idade: int, temperatura: float, possui_doenca_cronica: str):
    pacientes.append = (nome, idade, temperatura, possui_doenca_cronica)
    for i in range(len(pacientes)):
        print(pacientes[i])


def interface_triagem():
    try:
        while True:
            print('\n'
                  '===== TRIAGEM DE PACIENTES ====='
                  '\n')
            while True:
                nome = input('Digite o nome do paciente: ')
                if nome in '1234567890':
                    print('Erro! Use somente caracteres afabéticos.')
                else:
                    break
            while True:
                idade = int(input('Idade: '))
                if idade < 0:
                    print('Erro! Digite um número inteiro positivo.')
                else:
                    break
            while True:
                temperatura = float(input('Digite a temperatura: '))
                break
            while True:
                possui_doenca_cronica = str(input("Possui doença cronica? [S/N] "))
                if possui_doenca_cronica.upper() == 'S' and len(possui_doenca_cronica) == 1:
                    possui_doença_cronica = True
                    break
                elif possui_doenca_cronica.upper() == 'N' and len(possui_doenca_cronica) == 1:
                    possui_doença_cronica = False
                    break
                else:
                    print("Erro! Digite 'S' para Sim ou 'N' para Não.")
            # cadastra_paciente(nome, idade, temperatura, possui_doenca_cronica)
    except:
        print()

interface_triagem()