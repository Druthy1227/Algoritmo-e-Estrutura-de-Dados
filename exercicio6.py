# Tupla para os nomes
opcoes_nomes = (
    'Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro'
)

# Lista para armazenar as contagens (índice 0 não é usado)
votos_contagem = [0] * 7
total_votos = 0

print("Enquete: Qual o melhor SO? (1-6 ou 0 para sair)")

# Loop de leitura
while True:
    voto = int(input("Voto: "))
    
    # 1. Verifica a condição de parada
    if voto == 0:
        break # Encerra o loop
        
    # 2. VALIDAÇÃO DE ENTRADA
    # Verifica se o voto está fora do intervalo permitido (1 a 6)
    if voto < 1 or voto > 6:
        print("Valor inválido! Digite apenas um número entre 1 e 6 (ou 0 para sair).")
        continue # Pula para a próxima iteração, ignorando o voto inválido
    
    # Se o código chegou aqui, o voto é válido (1-6)
    votos_contagem[voto] = votos_contagem[voto] + 1
    total_votos = total_votos + 1

# Processamento e Exibição
print("\n--- Resultado da Enquete ---")
print("Sistema Operacional   Votos     %")
print("-------------------   -----   -----")

maior_voto_contagem = -1
maior_voto_indice = -1

# Garante que não haja divisão por zero se nenhum voto for computado
if total_votos > 0:
    for i in range(1, 7):
        nome_so = opcoes_nomes[i-1]
        votos_so = votos_contagem[i]
        
        percentual = (votos_so / total_votos) * 100
            
        print(f"{nome_so:<19} {votos_so:>5}   {percentual:>6.0f}%")
        
        # Verifica o vencedor
        if votos_so > maior_voto_contagem:
            maior_voto_contagem = votos_so
            maior_voto_indice = i

    print("-------------------   -----")
    print(f"Total                 {total_votos:>5}")

    # Exibe o vencedor
    nome_vencedor = opcoes_nomes[maior_voto_indice - 1]
    perc_vencedor = (maior_voto_contagem / total_votos) * 100
    print(f"\nO Sistema Operacional mais votado foi o {nome_vencedor}, com {maior_voto_contagem} correspondendo a ({perc_vencedor:.0f}%) dos votos.")
else:
    print("-------------------   -----")
    print(f"Total                 {total_votos:>5}")
    print("\nNenhum voto foi computado.")