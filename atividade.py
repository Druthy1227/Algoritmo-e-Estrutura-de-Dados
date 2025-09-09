
peso = float(input("Insira o peso dos peixes:"))  # Input do peso total dos peixes
excesso = peso - 40 # Cálculo do excesso caso venha a existir 

if excesso > 0: # Caso o excesso seja um valor positivo maior do que 0, irá printar uma mensagem o volume e a multa
    print(f"O excesso é de {excesso}kg, então você irá pagar {excesso*5} reais!")
else:
    print(f"Não existe excesso de peso") # Caso não, irá sinalizar que está no limite


print(f"O peso dos peixes que João pescou foi de {peso} kg") # Print da menssagem com o peso, independente de excesso