# Lista pré-definida de cidades
cidades = ["Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte", 
           "Florianópolis", "Recife", "Fortaleza", "Manaus"]

# Solicita ao usuário uma letra ou sequência de caracteres
busca = input("Digite uma letra ou sequência de caracteres para buscar nas cidades: ")

# Filtra as cidades que contêm a sequência, ignorando maiúsculas/minúsculas
resultado = [cidade for cidade in cidades if busca.lower() in cidade.lower()]

# Exibe o resultado
if resultado:
    print("Cidades encontradas:")
    for cidade in resultado:
        print("-", cidade)
else:
    print("Nenhuma cidade corresponde ao critério de busca.")
