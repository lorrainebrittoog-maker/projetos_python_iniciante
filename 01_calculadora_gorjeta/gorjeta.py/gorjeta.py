valor_compras = float(input("Valor total da compra: "))


print("Qual foi a qualidade do atendimento?")

print("1 - Péssimo... (0% de gorjeta)")
print("2 - Ruim (5% de gorjeta)")
print("3 - Agradável (10% de gorjeta)")
print("4 - Excelente! (15% de gorjeta)")

qualidade = int(input("Digite o número da opção correspondente: "))
print("Muito obrigado!")

if qualidade == 1:
    gorjeta = valor_compras * 0
    input("Por favor, nos de um feedback para nos ajudar a melhorar: ")
elif qualidade == 2:
    gorjeta = valor_compras * 0.05
    input("Por favor, nos de um feedback para nos ajudar a melhorar: ")
elif qualidade == 3:
    gorjeta = valor_compras * 0.10
elif qualidade == 4:
    gorjeta = valor_compras * 0.15
else:
    print("Resposta inválida. A gorjeta não foi calculada")
    gorjeta = 0
 

print(f"Valor das compras: {valor_compras:.2f}")
print(f"Valor da gorjeta: {gorjeta:.2f}")
print(f"Valor total {valor_compras + gorjeta:.2f}")


