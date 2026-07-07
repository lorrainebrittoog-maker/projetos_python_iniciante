p1 = float(input("Valor do Produto 1: R$"))
p2 = float(input("Valor do Produto 2: R$"))
p3 = float(input("Valor do Produto 3: R$"))

total = (p1 + p2 + p3)
bruto = print(f"O valor sem desconto é R${total:.2f}.")


if total >= 100:
    retirar = (total * 10)/100
    porcentagem = "10%"
elif total >= 50:
    retirar = (total * 5)/100
    porcentagem = "5%"
else:
    porcentagem = "0%"



