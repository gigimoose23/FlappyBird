import pygame,sys,random
pygame.init()
gameRunning = True
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
        global gameRunning
        if gameRunning:
            self.imageCooldown +=1
            if self.imageCooldown >= 6:
                if self.imageIndex == 2:
                    self.imageIndex = -1
                self.imageCooldown= 0
                self.imageIndex+=1
            self.image = self.images[self.imageIndex]
            self.image = pygame.transform.rotate(self.image, -self.vel*2)
            self.vel+=0.5
            if self.rect.y <= HEIGHT - 130 and self.rect.y >= 0:
                
                self.rect.y += self.vel
            else:
                gameRunning = False
            if  pygame.mouse.get_pressed()[0] == 1 and self.goingUp == False :
                self.goingUp = True
                self.vel =-5
            else:
                
                self.goingUp = False

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,flipped) -> None:
        pygame.sprite.Sprite.__init__(self)
     
       
        self.image = pygame.image.load("images/pipe.png")
        self.rect:pygame.Rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.vel = 0
        self.flipped = flipped
        if self.flipped:
            self.image = pygame.transform.flip(self.image, False, True)
        
    def update(self):
        if gameRunning:
            self.rect.x -= 5
        
WIDTH = 600
HEIGHT = 600
fps = 30
BirdMain=Bird(50,50)

BirdGroup = pygame.sprite.Group()
PipeGroup = pygame.sprite.Group()

BirdGroup.add(BirdMain)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bgImage = pygame.image.load("images/bg.png")
groundImage = pygame.image.load("images/ground.png")
groundPos = 0
pipeCooldown = 0
recentTouchedPipe = False
recentPipe = None
def drawN():
    screen.blit(bgImage, (0,-50))
    screen.blit(groundImage, (groundPos,HEIGHT - 100))
    PipeGroup.draw(screen)
    PipeGroup.update()
    BirdGroup.draw(screen)
    BirdGroup.update()
running = True

while running:

    if not groundPos == -290:
        if gameRunning:
            groundPos -= 10
    
    else:
        groundPos = 0

    if gameRunning:
        pipeCooldown+=1
        
        if pygame.sprite.groupcollide(BirdGroup, PipeGroup, False, False):
            gameRunning = False
        if pipeCooldown == 100:
            pipeCooldown = 0
            recentTouchedPipe = False
            randomHeight = random.randint(-100,100)
            PipeBottom = Pipe(700,HEIGHT + randomHeight, 0)
            PipeTop = Pipe(700,-20 + randomHeight - 50, 1)
            recentPipe = PipeTop
            PipeGroup.add(PipeTop)
            PipeGroup.add(PipeBottom)
        if recentPipe != None:
            
            if BirdGroup.sprites()[0].rect.left >= recentPipe.rect.right and not recentTouchedPipe:
                recentTouchedPipe = True
                print("passed pipe")


        
   
    drawN()

    pygame.time.Clock().tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            sys.exit(0)
            pygame.quit()
    pygame.display.flip()

