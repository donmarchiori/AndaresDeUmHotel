import datetime  # Importa o módulo datetime para lidar com datas

def calcular_idade(ano_nascimento):
    # Função para calcular a idade com base no ano de nascimento
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    # Função para obter o ano de nascimento do usuário, tratando exceções
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922 a 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um ano válido.")

def main():
    # Função principal do programa
    nome_completo = input("Digite seu nome completo: ")

    ano_nascimento = obter_ano_nascimento()

    idade = calcular_idade(ano_nascimento)

    print(f"Olá, {nome_completo}!")
    print(f"Você completou ou completará {idade} anos no ano de 2022.")

if __name__ == "__main__":
    main()