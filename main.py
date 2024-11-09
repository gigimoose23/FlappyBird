import pygame,sys
pygame.init()
class Bird(pygame.sprite.Sprite):
    
    def __init__(self,x,y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.imageIndex = 0
        self.imageCooldown = 0
        self.goingUp = False
        self.images = []
        toLoadImgs = ["birdwingsdown.png", "birdswingstable.png", "birdwingsup.png"]
        for imageName in toLoadImgs:
            self.images.append(pygame.image.load("images/" + imageName))
        self.image = self.images[self.imageIndex]
        self.rect:pygame.Rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.vel = 0
        
        
    def update(self):
        
        self.imageCooldown +=1
        if self.imageCooldown >= 6:
            if self.imageIndex == 2:
                self.imageIndex = -1
            self.imageCooldown= 0
            self.imageIndex+=1
        self.image = self.images[self.imageIndex]
        self.image = pygame.transform.rotate(self.image, -self.vel*2)
        self.vel+=0.5
        if self.rect.y <= HEIGHT - 130:
            self.rect.y += self.vel
        if  pygame.mouse.get_pressed()[0] == 1 and self.goingUp == False :
            self.goingUp = True
            self.vel =-5
        else:
            
            self.goingUp = False
        
WIDTH = 600
HEIGHT = 600
fps = 30
BirdMain=Bird(50,50)
BirdGroup = pygame.sprite.Group()
BirdGroup.add(BirdMain)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bgImage = pygame.image.load("images/bg.png")
groundImage = pygame.image.load("images/ground.png")
groundPos = 0
def drawN():
    screen.blit(bgImage, (0,-50))
    screen.blit(groundImage, (groundPos,HEIGHT - 100))
running = True
while running:
    if not groundPos == -290:
        groundPos -= 10
    else:
        groundPos = 0
   
    drawN()
    BirdGroup.draw(screen)
    BirdGroup.update()
    pygame.time.Clock().tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            sys.exit(0)
            pygame.quit()
    pygame.display.flip()

