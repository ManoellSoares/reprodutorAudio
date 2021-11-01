import pygame

pygame.mixer.init()
pygame.init()


tela = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Reprodutor de Música")
black = (0, 0, 0)

pygame.mixer.music.load('nomeDoAudio.mp3')
pygame.mixer.music.play()
pygame.event.wait()

pausar = False
run = True
volume = 1

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_a:
                pygame.mixer.music.play()
            elif event.key == pygame.K_q:
                if pausar == False:
                    pygame.mixer.music.pause()
                    pausar = True
                else: 
                    pygame.mixer.music.unpause() 
                    pausar = False
            elif event.key == pygame.K_UP:
                volume = volume + 0.1
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_DOWN:
                volume = volume - 0.1 
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_x:
                pygame.quit()       

    tela.fill(black)
    pygame.display.update()
