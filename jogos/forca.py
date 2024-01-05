def jogar():
    
    print("*************************************")
    print("*****Bem vindo ao jogo de Forca!*****")
    print("*************************************")

    palavra_secreta = "python".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
        
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
   
    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
            index += 1
        
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        print("Você ganhou!!!")
    
    else:
        print("Você perdeu!!!")
    
    print("Fim do Jogo")

if __name__ == "__main__":
    jogar()