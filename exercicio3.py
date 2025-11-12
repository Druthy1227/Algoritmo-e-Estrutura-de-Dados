import array

meses_do_ano = (
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
)

# Abre o vetor de temperaturas
vetor_temps = array.array(
    "f", [0.0] * 12
)  # Listagem baseada na quantidade de meses_do_ano
soma_temps = 0.0  # Soma das temperaturas armazenada em uma única variável

# Leitura e soma
print("Digite as temperaturas médias de cada mês:")
for i in range(12):  # Range = Número de meses
    vetor_temps[i] = float(input(f"Temperatura de {meses_do_ano[i]}: "))
    soma_temps = soma_temps + vetor_temps[i]  # Adiciona a temperatura lida à soma total

# Cálculo da média
media_anual = soma_temps / 12
print(f"\nMédia Anual: {media_anual:.2f} °C")

# Verificação
print("\nTemperaturas Acima da Média:")
for i in range(12):
    if vetor_temps[i] > media_anual:  # Vetpr i é comparado com a media_anual
        print(
            f"{meses_do_ano[i]}: {vetor_temps[i]:.2f} - Diferença de: {vetor_temps[i]-media_anual:.2f} °C!"
        )  # Bônus: Diferença entre a temperatura do mês e a média anual