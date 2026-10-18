
from colorama import init, Fore, Style

# Inicializa a biblioteca Colorama
init()

# Lista com os níveis e as situações do reservatório
niveis_agua = [
    (1, "Muito baixo (crítico)", Fore.RED),
    (2, "Baixo", Fore.YELLOW),
    (3, "Médio", Fore.GREEN),
    (4, "Alto", Fore.CYAN),
    (5, "Muito alto (alerta)", Fore.BLUE)
]

# Função que exibe a mensagem com a cor correspondente
def exibir_nivel(nivel):
    for numero, situacao, cor in niveis_agua:
        if numero == nivel:
            print(f"{cor}Nível {numero}: {situacao}{Style.RESET_ALL}")
            return

    print("Nível inválido!")


# Simulação do monitoramento do reservatório
for numero, situacao, cor in niveis_agua:
    exibir_nivel(numero)
