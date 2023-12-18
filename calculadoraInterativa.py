def calculadora_interativa():
    # Função que implementa uma calculadora interativa
    while True:
        # Início de um loop infinito para manter a calculadora em execução até que o usuário escolha sair
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        # Exibição do menu de operações disponíveis
        
        try:
            operacao = int(input("Escolha a operação (0 a 4): "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        # Tenta converter a entrada do usuário para um número inteiro, tratando exceção se a conversão falhar

        if operacao == 0:
            print("Saindo da calculadora. Até mais!")
            break
        # Se o usuário escolher 0, imprime uma mensagem de saída e interrompe o loop com a instrução 'break'

        elif operacao in range(1, 5):
            # Se a escolha do usuário estiver no intervalo de 1 a 4 (inclusive)
            
            try:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))
            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
                continue
            # Tenta converter as entradas do usuário para números de ponto flutuante, tratando exceção se a conversão falhar

            if operacao == 1:
                resultado = num1 + num2
            elif operacao == 2:
                resultado = num1 - num2
            elif operacao == 3:
                resultado = num1 * num2
            elif operacao == 4:
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero. Resultado: 0")
                    continue
            # Realiza a operação escolhida pelo usuário, tratando divisão por zero

            print("Resultado:", resultado)
            # Imprime o resultado da operação

        else:
            print("Essa opção não existe. Por favor, escolha uma opção válida.")
        # Se a escolha do usuário não estiver no intervalo de 0 a 4, exibe uma mensagem de erro

if __name__ == "__main__":
    calculadora_interativa()
    # Chama a função calculadora_interativa() se o script for executado como programa principal
