def inicio():
    print('Iniciando menu')
    print("Menu iniciado")
    print('Onde você quer começar?')

    comeco = int(input('1 - Escola, 2 - Floresta, 3 - Em casa\n> '))
    if comeco == 1:
        escola()
    elif comeco == 2:
        floresta()  # CORREÇÃO 1: Adicionado para o menu inicial conseguir ir para a floresta!
    elif comeco == 3:
        casa()


def escola():
    na_escola = True

    while na_escola:
        print("\n--- Você está dentro da ESCOLA ---")
        print("O que você quer fazer?")
        print("1 - Estudar")
        print("2 - Passear")
        print("3 - Dormir na aula")
        print("4 - Ir para a Floresta")
        print("5 - Ir para Casa")
        print("6 - Voltar ao Menu Inicial")

        escolha = int(input("> "))

        if escolha == 1:
            print("\nQual matéria você quer estudar?")
            estudando = True
            while estudando:
                decisao1 = int(input("1 - Matemática, 2 - Ciencias, 3 - Inglês, 4 - Sair\n> "))

                if decisao1 == 1:
                    print("Você estudou frações e equações. Ficou mais inteligente!")
                elif decisao1 == 2:
                    print("Você estudou sobre células e plantas na aula de Ciências.")
                elif decisao1 == 3:
                    print("You practiced your English! Muito bem.")
                elif decisao1 == 4:
                    print("Saindo da sala de estudos...")
                    estudando = False

        elif escolha == 2:
            print("\nVocê está passeando pela escola quando vê muitas pessoas conversando no corredor.")

        elif escolha == 3:
            print("\nVocê dormiu na aula... O sinal tocou e o inspetor te mandou direto para casa!")
            na_escola = False
            casa()

        elif escolha == 4:
            print("Saindo da escola e indo para a Floresta...")
            na_escola = False
            floresta()  # Conectado!

        elif escolha == 5:
            print("Saindo da escola e indo para Casa...")
            na_escola = False
            casa()

        elif escolha == 6:
            print("Voltando para o Menu Inicial...")
            na_escola = False
            inicio()


def casa():
    em_casa = True

    while em_casa:
        print("\n--- Você está dentro de CASA ---")
        print("O que você quer fazer?")
        print("1 - Estudar")
        print("2 - Jogar videogame")
        print("3 - Dormir")
        print("4 - Ir para a Floresta")
        print("5 - Voltar para a Escola")
        print("6 - Voltar ao Menu Inicial")

        escolha_casa = int(input("> "))
        if escolha_casa == 1:
            print("\nQual matéria você quer estudar?")
            estudando = True
            while estudando:
                decisao1 = int(input("1 - Matemática, 2 - Ciencias, 3 - Inglês, 4 - Sair\n> "))
                if decisao1 == 1:
                    print("Você estudou frações e equações. Ficou mais inteligente!")
                elif decisao1 == 2:
                    print("Você estudou sobre células e plantas na aula de Ciências.")
                elif decisao1 == 3:
                    print("You practiced your English! Muito bem.")
                elif decisao1 == 4:
                    print("Parando de estudar...")
                    estudando = False

        elif escolha_casa == 4:
            print("Saindo de casa e indo para a floresta...")
            em_casa = False
            floresta()  # Conectado!

        elif escolha_casa == 5:
            print("Arrumando a mochila para voltar à escola...")
            em_casa = False
            escola()

        elif escolha_casa == 6:
            print("Voltando ao menu inicial...")
            em_casa = False
            inicio()


# CORREÇÃO 2: A def floresta() agora está totalmente alinhada na esquerda!
def floresta():
    em_floresta = True

    while em_floresta:
        print("\n--- Você está na FLORESTA ---")
        print("O que você quer fazer?")
        print("1 - Caçar")
        print("2 - Pescar")
        print("3 - Pegar madeira")
        print("4 - Ir para a Escola")
        print("5 - Ir para Casa")
        print("6 - Voltar ao Menu Inicial")

        escolha_floresta = int(input("> "))

        if escolha_floresta == 1:
            print("\nO que você vai tentar caçar hoje?")
            cacar = True
            while cacar:
                decisao2 = int(input("1 - Porco, 2 - Javali, 3 - Vaca, 4 - Sair\n> "))

                if decisao2 == 1:
                    print("Você caçou um porco e adquiriu muita carne!")
                elif decisao2 == 2:
                    print("Você caçou um javali e obteve couro, carne e chifres.")
                elif decisao2 == 3:
                    print("Você caçou uma vaca e pegou couro e carne.")
                elif decisao2 == 4:
                    print("Parando de caçar...")
                    cacar = False

        elif escolha_floresta == 4:
            print("Saindo da floresta e indo para a Escola...")
            em_floresta = False
            escola()

        elif escolha_floresta == 5:
            print("Saindo da floresta e indo para Casa...")
            em_floresta = False
            casa()

        elif escolha_floresta == 6:
            print("Voltando ao menu inicial...")
            em_floresta = False
            inicio()


# --- COMANDO PARA O JOGO COMEÇAR ---
inicio()