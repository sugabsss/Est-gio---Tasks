def main():
    palavra = input("Escreva uma palavra:").lower().strip()

    letra = 'a'
    i = 0

    if letra in palavra:
        print(f"{letra} Encontrada na palavra!")

        for j in palavra:
            if j == letra:
                i+= 1

        print(f"Letra ({letra}) Foi Encotrada {i} Vezes na palavra")

    else:    
        print(f"Letra ({letra}) Não encontrada na palavra!")

main()