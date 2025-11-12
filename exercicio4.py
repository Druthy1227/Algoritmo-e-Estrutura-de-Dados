import array

tamanho_vetor = int((input("Quantos números terá o vetor?: ")))  # Recebe o tamanho do vetor
vetor = array.array("i", [0] * tamanho_vetor)  # Abre o vetor de 20 números -->inteiros<--

print("Digite os valores do vetor:")  # recebe todos os 20 vetores
for i in range(tamanho_vetor):
    vetor[i] = int(input(f"Posição {i+1}: "))

print(
    f"Vetor Original: {list(vetor)}"
)  # Mostra o vetor original, completo mas desordenado.

# A partir daqui todo o vetor já existe.
for i in range(tamanho_vetor):
          # Range(20) pode ser facilmente alterado para range(len(vetor)), uma vez que a função len se refere a lenghth (comprimento/tamanho)
    indice_menor = (
        i  # Índice alvo para ser organizado, começando pelo início do vetor (índice 0)
    )

    for k in range(
        i + 1, tamanho_vetor
    ):  # Le o comment de cima, vale pro mesmo 20 após a vírgula || Varrer o vetor a partir da posição i+1 até o final, em caso de i,20 geraria apenas uma auto-comparação.
        if (
            vetor[k] < vetor[indice_menor]
        ):  # Se o vetor de indice k for MENOR que o valor do indice_menor, atualiza o indice_menor
            indice_menor = k  # Atualiza o indice_menor para o indice k, que é o menor valor encontrado até agorae o atribui na variável indice_menor

    # SWAP (Troca)
    temp = vetor[
        i
    ]  # Armazena temporariamente o valor original do vetor na posição i || vetor[i] || em uma variável externa.
    vetor[i] = vetor[
        indice_menor
    ]  # O vetor[i] de fato agora está recebendo o valor do vetor[indice_menor], que é o menor valor encontrado no ciclo "k", ou seja, o vetor[indice_menor] existirá em duas instâncias.
    vetor[indice_menor] = (
        temp  # Atribui o valor temp (original da posição i) para a posição do indice_menor (índice que foi extraído e "clonado" na posição i).
    )

print(f"Vetor Ordenado: {list(vetor)}")

  # SWAP (Troca) - Exemplo prático:

  # --- SIMULAÇÃO DO CICLO 1 ---

  # ESTADO INICIAL DO VETOR: [8, 5, 9, 2]
  # O loop 'i' começa. O objetivo é arrumar a posição de índice 0 (a primeira posição).

  # for i in range(4): --> i = 0

  #     indice_menor = i --> indice_menor = 0 (valor 8)

  #     # for k in range(i + 1, 4):
  #          k=1: if vetor[1] (5) < vetor[0] (8)? SIM.
  #               indice_menor é atualizado para 1. (apenas a variável indice_menor é alterada, o vetor permanece o mesmo)

  #          k=2: if vetor[2] (9) < vetor[1] (5)? NÃO.
  #               indice_menor continua 1.
  #
  #          k=3: if vetor[3] (2) < vetor[1] (5)? SIM.
  #               indice_menor é atualizado para 3. (apenas a variável indice_menor é alterada, o vetor permanece o mesmo)

  #     # O loop 'k' termina.
  #     # 'i' ainda é 0.
  #     # 'indice_menor' (posição do menor valor) é 3.
  #     indice_menor = 3 --> decorrente da última comparação.

  #     # "Troca" o valor da posição 'i' (vetor[0]) com o valor da posição 'indice_menor' (vetor[3]).
  #     temp = vetor[i]
  #     temp = vetor[0] (temp = 8)

  #     vetor[i] = vetor[indice_menor]
  #     vetor[0] = vetor[3] (vetor[0] = 2)

  #     vetor[indice_menor] = temp
  #     # vetor[3] = temp (vetor[3] = 8)

  # ESTADO FINAL DO CICLO 1: [2, 5, 9, 8]
