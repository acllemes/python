import sys, pygame # biblioteca usada para criar o jogo 

pygame.init() # onde se inicia o jogo 

size = width, height = 650, 480 # aqui muda o tamanho da tela do jogo
dx = 1 # direção da bola
dy = 1 # direção da bola 
x= 163 # 
y = 120 # 
black = (50,50,50) # aqui deixa o fundo da tela mais preto ou mais branco
white = (255,255,50) # aqui muda a cor da bola 

screen = pygame.display.set_mode(size)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += dx
    y += dy

    if x < 0 or x > width:   
        dx = -dx

    if y < 0 or y > height:
        dy = -dy

    screen.fill(black)

    pygame.draw.circle(screen, white, (x,y), 8)

    pygame.display.flip()