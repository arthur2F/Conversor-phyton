# Conversor de Temperatura

temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade (C ou F): ").upper()

if unidade == "C":
    # Celsius para Fahrenheit
    convertido = (temperatura * 9/5) + 32
    print(f"{temperatura}°C = {convertido:.2f}°F")

elif unidade == "F":
    # Fahrenheit para Celsius
    convertido = (temperatura - 32) * 5/9
    print(f"{temperatura}°F = {convertido:.2f}°C")

else:
    print("Unidade inválida! Use apenas C ou F.")