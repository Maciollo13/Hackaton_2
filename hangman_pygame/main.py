import pygame

# initializing and setting up display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# upload images
images = []
for i in range(7):
    image = pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

# variables
hangman_image = 0
WHITE = (255, 255, 255)

# button variables
RADIUS = 20
GAP = 15
start_x = round((WIDTH-(RADIUS * 2 + GAP)* 13)/ 2)
start_y = 400
for i in range(26):
    x = start_x + GAP * 2 + ((RADIUS *2 + GAP) * (i % 13))
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))
# Game loop
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)  # this defines speed of refresh of the game
    win.fill(WHITE)
    win.blit(images[hangman_image], (120,70))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)





pygame.quit()
