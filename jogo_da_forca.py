import os

def mostrar_forca(erros):
    estagios = [
        """
           ------
           |    |
           |    
           |   
           |   
           |  
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |  
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |  
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |  
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |  
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |  
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |  
        """
    ]
    print(estagios[erros])

def jogar():
    palavras = ["python", "computador", "programacao", "desenvolvimento"]
    palavra_secreta = palavras[0].upper()  # Escolhendo a primeira palavra e colocando em maiúsculas
    palavra_oculta = "_" * len(palavra_secreta)
    
    tentativas = 0
    letras_usadas = []
    
    while tentativas < 6 and palavra_oculta != palavra_secreta:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_forca(tentativas)
        print(f"\nPalavra: {' '.join(palavra_oculta)}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        
        tentativa = input("\nDigite uma letra: ").lower()
        
        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Por favor, insira apenas uma letra.")
            continue
        
        if tentativa in letras_usadas:
            print("Você já tentou essa letra!")
            continue
        
        letras_usadas.append(tentativa)
        
        if palavra_secreta.find(tentativa.upper()) != -1:  
            palavra_oculta = "".join([
                tentativa.upper() if palavra_secreta[i] == tentativa.upper() else palavra_oculta[i]
                for i in range(len(palavra_secreta))
            ])
        else:
            tentativas += 1
    
    os.system("cls" if os.name == "nt" else "clear")
    mostrar_forca(tentativas)

    if palavra_oculta == palavra_secreta:
        print("\nParabéns! Você acertou a palavra:", palavra_secreta)
    else:
        print("\nGame Over! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogar()
