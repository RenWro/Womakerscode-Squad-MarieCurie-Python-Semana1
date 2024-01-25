# Desenvolver um programa  que solicite  a idade do usuário e identifique se ele é uma criança , um adolescente, adulto ou idoso.

def classificar_idade(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade <= 13:
        return "Criança"
    elif idade > 13 and idade < 18:
        return "Adolescente"
    elif idade >= 18 and idade <= 60:
        return "Adulto"
    else:
        return "Idoso"

def main():
    try:
        idade = int(input("Digite sua idade: "))
        classificacao = classificar_idade(idade)
        print(f"Você é classificado como {classificacao}.")
    except ValueError:
        print("Por favor, insira uma idade válida.")

if __name__ == "__main__":
    main()
