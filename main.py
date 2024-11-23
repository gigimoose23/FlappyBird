import pygame,sys,random
pygame.init()
gameRunning = True
score = 0
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
        self.passed = False
        if self.flipped:
            self.image = pygame.transform.flip(self.image, False, True)

    def update(self):
        global score
        if gameRunning:
            self.rect.x -= 5
            if self.flipped:
                if not self.passed and self.rect.right < BirdMain.rect.left:
                    
                    self.passed = True
                    score+=1

        
WIDTH = 600
HEIGHT = 600
fps = 30
BirdMain=Bird(50,50)

BirdGroup = pygame.sprite.Group()
PipeGroup = pygame.sprite.Group()

BirdGroup.add(BirdMain)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bgImage = pygame.image.load("images/bg.png")
restartImage = pygame.image.load("images/btnrestart.png")
restartRect = pygame.Rect((HEIGHT / 2)-70, (WIDTH/2)-90,120,42)
scoreText = pygame.font.SysFont("Arial", 25, True)

groundImage = pygame.image.load("images/ground.png")
groundPos = 0
pipeCooldown = 0

recentPipe = None
def drawN():
    screen.blit(bgImage, (0,-50))
    screen.blit(groundImage, (groundPos,HEIGHT - 100))
    
    PipeGroup.draw(screen)
    PipeGroup.update()
    BirdGroup.draw(screen)
    BirdGroup.update()
    textS = scoreText.render("Score: " + str(score),True,(255,255,255))
    screen.blit(textS, (0,0))
    if not gameRunning:


        screen.blit(restartImage, ((HEIGHT / 2)-70, (WIDTH/2)-90))

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
      
            randomHeight = random.randint(-100,100)
            PipeBottom = Pipe(700,HEIGHT + randomHeight, 0)
            PipeTop = Pipe(700,-20 + randomHeight - 50, 1)
            recentPipe = PipeTop
            PipeGroup.add(PipeTop)
            PipeGroup.add(PipeBottom)
        if recentPipe != None:
           # print(str(BirdGroup.sprites()[0].rect.left) + " vs " + str(recentPipe.rect.left))
            
            if BirdGroup.sprites()[0].rect.left >= recentPipe.rect.left:
           
                print("passed pipe")


        
   
    drawN()

    pygame.time.Clock().tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            sys.exit(0)
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if not gameRunning and restartRect.collidepoint(event.pos[0],event.pos[1]):
                print("we wanna res")
                BirdMain.vel = 0
                BirdMain.rect.center = (50,50)
                PipeGroup.spritedict = {}
                score = 0
                gameRunning = True
    pygame.display.flip()
        
            

