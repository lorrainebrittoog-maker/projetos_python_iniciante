print("Vamos calcular seu Índice de Massa Corporal (IMC)?")

peso = float(input("Digite seu peso em kg: ")) 
altura = float(input("Digite sua altura em metros: "))

resumo = peso / altura**2

if resumo < 18.5:
    print(f"Seu IMC é {resumo:.2f}, que é considerado abaixo do peso.")
elif 18.5 <= resumo <= 24.9:
    print(f"Seu IMC é {resumo:.2f}, que é considerado um peso saúdavel.")
elif 25 <= resumo <= 29.9:
    print(f"Seu IMC é {resumo:.2f}, que é considerado sobrepeso.")
elif 30 <= resumo <= 34.9:
    print(f"Seu IMC é {resumo:.2f}, que é considerado obesidade grau 1")
elif 35 <= resumo <= 39.9:
    print(f"Seu IMC é {resumo:.2f}, que é considerado obesidade grau 2")
else: 
    print(f"Seu IMC é {resumo:.2f}, que é considerado obesidade grau 3")




















