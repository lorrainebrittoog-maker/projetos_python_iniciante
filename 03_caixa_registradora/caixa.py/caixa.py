p1 = float(input("Valor do Produto 1: R$"))
p2 = float(input("Valor do Produto 2: R$"))
p3 = float(input("Valor do Produto 3: R$"))

total = (p1 + p2 + p3)
print(f"O valor sem desconto é R${total:.2f}.")


if total >= 100:
    desconto = (total * 10)/100
    porcentagem = "10%"
elif total >= 50:
    desconto = (total * 5)/100
    porcentagem = "5%"
else:
    desconto = (total * 0)/100
    porcentagem = "0%"
    
a_ser_pago = total - desconto

print(f"Foi aplicado um desconto de: {porcentagem} -> R$ {a_ser_pago:.2f}")

entregue = (float(input("Valor entregue pelo cliente: R$ ")))

if a_ser_pago <= entregue:
    troco = entregue - a_ser_pago
    print(f"Troco: R$ {troco:.2f}")
else:
    falta = a_ser_pago - entregue
    print(f"Valor insuficiente. Falta R$ {falta:.2f}") 

