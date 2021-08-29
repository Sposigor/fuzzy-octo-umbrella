from main import inss_irrf

print("Calculadora de IRRF")
print("#"*35)

rendimento = float(input("Infome o salario para calcular o desconto de INSS e IRRF: "))

a, b = inss_irrf(rendimento)

print(f"Seu desconto de INSS é {b}, e o recolhimento IR é de {a}")