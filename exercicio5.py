import array
tamanho_vetor = int((input("Quantos números terá o vetor?: ")))
# Abre o vetor
vetor = array.array('i', [0] * tamanho_vetor)

# Request dos valroes
print("Digite os valores do vetor:")
for i in range(tamanho_vetor):
    vetor[i] = int(input(f"Posição {i+1}: "))

print(f"Vetor Original: {list(vetor)}")

for i in range(tamanho_vetor):
    for j in range(0, tamanho_vetor - i - 1): # O range começa em 0, e vai até o j = 2 pois caso fosse até o j =3 (quarto elemento), ocorreria um erro já que o j+1 no Swap iria ultrapassar o seu indexamento.
        if vetor[j] > vetor[j+1]:             # Compara o valor da esquerda com o da direita.
            temp  = vetor[j]                  # Guarda o valor da esquerda (ex: 8) em uma variável temporária.
            vetor[j] = vetor[j+1]             # Move o valor da direita (ex: 5) para a posição da esquerda. (Vetor: [5, 5])
            vetor[j+1] = temp                 # Pega o valor guardado (8) e o coloca na posição da direita. (Vetor: [5, 8])

print(f"Vetor Ordenado: {list(vetor)}")