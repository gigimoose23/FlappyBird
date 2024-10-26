import pygame,sys
pygame.init()
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        self.images = []
        toLoadImgs = ["birdwingsdown.png", "birdswingstable.png", "birdwingsup.png"]
        for imageName in toLoadImgs:
            self.images.append(pygame.image.load("images/" + imageName))
WIDTH = 600
HEIGHT = 600
fps = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bgImage = pygame.image.load("images/bg.png")
groundImage = pygame.image.load("images/ground.png")
groundPos = 0
def draw():
    screen.blit(bgImage, (0,-50))
    screen.blit(groundImage, (groundPos,HEIGHT - 100))
running = True
while running:
    if not groundPos == -290:
        groundPos -= 10
    else:
        groundPos = 0
    
    draw()
    pygame.time.Clock().tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            sys.exit(0)
            pygame.quit()
    pygame.display.flip()

