import random

def jogo_adivinhar():
    print("Bem-vinda ao jogo de adivinhacao")
    print("Tente adivinhar o numero:"
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentantivas = 10

    while tentativas < max_tentativas:
        try:
            palpite = int(input(f"Tentativa {tentativa + 1} / {max_tentativas}: Digite seu palpite: ))
            except ValueError:
                ptint("Por favor, digite um numero valido.")
                continue
            tentativas += 1;

            if palpite == numero_secreto:
                printf(f"Parabens, acertou o numero ! Voce acertou em {tentativas} tentativas")
                break
            elif palpite < numero_secreto:
                print("Numero eh maior")
            else:
                print("Numero eh menor")
        if tentativas == max_tentantivas and palpite != numero_secreto:
            