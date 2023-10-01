# Bibliotecas
import pygame
import time
import os


# Variaveis usandas no Projeto
PomodoroPausa = 60 * 5  # tempo da pausa
PomodoroEstudos = 60 * 25  # tempo do estudo
PomodoroIntervalo = 60  # tempo antes de comeca
# loop aonde acontece o Pomodoro
while True:
    # alternativas
    print("1: Pausa")  # Para tirar uma pausa
    print("2: Estudos")  # Para Estudar
    print("3: Fechar")  # Para fechar o programa

    # Onde determina sua escolha
    resposta = int(input("qual pomodoro voce escolhe?: "))
    # 1 = pausa, pausa de 5 minutos para descansar um pouco
    os.system('cls')  # Usado para limpar o terminal
    if resposta == 1:  # caso a resposta seja igual a 1
        time.sleep(1)  # o tempo de atraso para o proximo comando
        print("sua resposta foi Pausa", resposta)
        time.sleep(2)
        print("Pronto para começar?")
        time.sleep(2)
        os.system('cls')
        # um loop para mostra o progresso do tempo do pomodoro
        for i in range(PomodoroPausa):  # (+ 1 para dar o tempo exato)
            time.sleep(1)
            print(i)
        os.system('cls')  # Usado para limpar o terminal
        # Definindo o toque toque do promodoro
        pygame.mixer.init()   # Inicializa o mixer do pygame para reprodução de áudio
        # Carrega a música que será tocada (substitua 'tudo.mp3' pelo caminho do seu arquivo de música)
        pygame.mixer.music.load('tudo.mp3')
        pygame.mixer.music.play()
        # Aguarda que o usuário pressione Enter para parar a música (pausa a execução do programa)
        input("Pressione Enter para parar a música...")
        pygame.mixer.music.stop()  # Para a reprodução da música
        print('Intervalo aproveite')
        os.system('cls')  # Usado para limpar o terminal
        # loop do intervalo de 1 minuto (+ 1 para dar o tempo exato)
        print("Intervalo")
        for i in range(PomodoroIntervalo + 1):
            time.sleep(0.1)
            print(i)
        os.system('cls')  # Usado para limpar o terminal
    if resposta == 2:  # caso a resposta seja igual a 2
        time.sleep(1)  # o tempo de atraso para o proximo comando
        print("sua resposta foi Estudos", resposta)
        time.sleep(2)
        print("Pronto para começar?")
        time.sleep(2)
        print('Seus estudos estao prestes a comecar, entao se ajeite ai')
        os.system('cls')  # Usado para limpar o terminal
        for i in range(PomodoroEstudos + 1):  # (+ 1 para dar o tempo exato)
            time.sleep(1)
            print(i)
        os.system('cls')  # Usado para limpar o terminal
        pygame.mixer.init()
        pygame.mixer.music.load('tudo.mp3')
        pygame.mixer.music.play()
        input("Pressione Enter para parar a música...")
        pygame.mixer.music.stop()
        os.system('cls')  # Usado para limpar o terminal
        print('Intervalo aproveite')
        for i in range(PomodoroIntervalo + 1):  # (+ 1 para dar o tempo exato)
            time.sleep(1)
            print(i)
        os.system('cls')  # Usado para limpar o terminal
    if resposta != 1 and resposta != 2:
        break
# fim
