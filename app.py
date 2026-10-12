
# Função para validar as notas
def validar_notas(lista_notas):
    """Verifica se as notas estão entre 0 e 10."""
    for nota in lista_notas:
        if nota < 0 or nota > 10:
            return False
    return True


# Função para calcular a média
def calcular_media_lista(lista_notas):
    """Calcula a média aritmética de uma lista de notas."""
    if len(lista_notas) == 0:
        return None

    soma = sum(lista_notas)
    quantidade = len(lista_notas)

    return soma / quantidade


# Função para verificar a aprovação
def verificar_aprovacao(media, media_minima):
    """Verifica se o aluno foi aprovado ou reprovado."""
    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"


# Lista para armazenar as notas
notas = []

# Entrada inicial
nome = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")

# Definição da média mínima
media_minima = float(input("Digite a média mínima para aprovação: "))

print("\nDigite as notas uma por uma.")
print("Digite 'fim' para calcular o resultado.\n")

# Recebimento das notas
while True:
    entrada = input("Digite a nota (ou 'fim' para encerrar): ")

    if entrada.lower() == "fim":
        break

    # Verifica se a entrada é um número
    try:
        nota_atual = float(entrada)
    except ValueError:
        print("Entrada inválida! Digite um número ou 'fim'.")
        continue

    # Verifica se a nota está entre 0 e 10
    if not validar_notas([nota_atual]):
        print("Nota inválida! Digite um valor entre 0 e 10.")
        continue

    notas.append(nota_atual)

# Verificação e cálculo da média
if len(notas) > 0:
    media_final = calcular_media_lista(notas)

    if media_final is not None:
        status_aluno = verificar_aprovacao(
            media_final, media_minima
        )

        # Exibição do relatório
        print("\n--- RELATÓRIO DE DESEMPENHO ---")
        print(f"Aluno: {nome}")
        print(f"Disciplina: {disciplina}")
        print(f"Notas registradas: {notas}")
        print(f"Média Final: {media_final:.2f}")
        print(f"Situação: {status_aluno}")
        print("--------------------------------")
else:
    print("\nNenhuma nota foi informada.")
    print("É necessário inserir pelo menos uma nota.")
