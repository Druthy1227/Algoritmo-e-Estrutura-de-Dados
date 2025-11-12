import array

quantidade_grupo = int(input("Quantas pessoas estão no grupo?:"))

# Abre os vetores de idade e altura
idade = array.array("i", [0] * quantidade_grupo)
altura = array.array("f", [0.0] * quantidade_grupo)

soma_idade = 0
soma_idade = 0.0

for i in range(quantidade_grupo):
    print(f"\nPessoa: {i+1}")
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))

    soma_idade = soma_idade + idade[i]
    soma_idade = soma_idade + altura[i]

media_idades = soma_idade / quantidade_grupo
media_alturas = soma_idade / quantidade_grupo

print("Médias")
print(f"\nMédia de Idade: {media_idades}")
print(f"Média de Altura: {media_alturas:.2f}")
