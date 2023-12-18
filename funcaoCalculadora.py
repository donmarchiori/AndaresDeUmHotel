def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        # Verifica se o divisor (num2) não é zero para evitar divisão por zero
        return num1 / num2 if num2 != 0 else 0
    else:
        print("Operação inválida. Resultado: 0")
        return 0