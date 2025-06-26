# Lista com pelo menos 10 títulos de livros
livros = [
    "Dom Casmurro",
    "Grande Sertão: Veredas",
    "O Senhor dos Anéis",
    "Cem Anos de Solidão",
    "A Revolução dos Bichos",
    "Harry Potter e a Pedra Filosofal",
    "Orgulho e Preconceito",
    "O Pequeno Príncipe",
    "1984",
    "O Código Da Vinci"
]

# Solicita ao usuário uma palavra-chave
palavra_chave = input("Digite uma palavra ou sequência para buscar nos títulos: ").lower()

# Filtra os títulos que contêm a palavra-chave, ignorando maiúsculas/minúsculas
resultados = [titulo for titulo in livros if palavra_chave in titulo.lower()]

# Exibe os resultados encontrados
if resultados:
    print("\nTítulos encontrados:")
    for titulo in resultados:
        print(f"- {titulo}")
else:
    print("\nNenhum título corresponde à sua busca.")
