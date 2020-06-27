import pygame

pygame.init()

EwalkLeft = [pygame.image.load("character/L1E.png"),pygame.image.load("character/L2E.png"),\
            pygame.image.load("character/L3E.png"),pygame.image.load("character/L4E.png"),\
            pygame.image.load("character/L5E.png"),pygame.image.load("character/L6E.png"),\
            pygame.image.load("character/L7E.png"),pygame.image.load("character/L8E.png"),\
            pygame.image.load("character/L9E.png"),pygame.image.load("character/L10E.png"),\
            pygame.image.load("character/L11E.png") ]

EwalkRight = [pygame.image.load("character/R1E.png"),pygame.image.load("character/R2E.png"),\
            pygame.image.load("character/R3E.png"),pygame.image.load("character/R4E.png"),\
            pygame.image.load("character/R5E.png"),pygame.image.load("character/R6E.png"),\
            pygame.image.load("character/R7E.png"),pygame.image.load("character/R8E.png"),\
            pygame.image.load("character/R9E.png"),pygame.image.load("character/R10E.png"),\
            pygame.image.load("character/R11E.png") ]

walkRight = [pygame.image.load("character/R1.png"),pygame.image.load("character/R2.png"),\
            pygame.image.load("character/R3.png"),pygame.image.load("character/R4.png"),\
            pygame.image.load("character/R5.png"),pygame.image.load("character/R6.png"),\
            pygame.image.load("character/R7.png"),pygame.image.load("character/R8.png"),\
            pygame.image.load("character/R9.png") ]

walkLeft = [pygame.image.load("character/L1.png"),pygame.image.load("character/L2.png"),\
            pygame.image.load("character/L3.png"),pygame.image.load("character/L4.png"),\
            pygame.image.load("character/L5.png"),pygame.image.load("character/L6.png"),\
            pygame.image.load("character/L7.png"),pygame.image.load("character/L8.png"),\
            pygame.image.load("character/L9.png") ]

bg = pygame.image.load("character/bg.jpg")
char = pygame.image.load("character/standing.png")

bulletsound = pygame.mixer.Sound("character/bullet.wav")
hitsound = pygame.mixer.Sound("character/hit.wav")
music = pygame.mixer.music.load("character/music.mp3")
pygame.mixer.music.play(-1)
score = 0
screen_height = 480
screen_width = 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First Game')


class player(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 5
        self.right = False
        self.left = False
        self.standing = True
        self.isJump = False
        self.Jumpcount = 6
        self.walkcount = 0
        self.box = (self.x + 16, self.y + 12, 32, 48)


    def draw(self,win):
        if man.walkcount >= 27:
            man.walkcount = 0

        if not man.standing:
            if man.left:
                win.blit(walkLeft[man.walkcount//3], (man.x,man.y))
                man.walkcount += 1

            elif man.right:
                win.blit(walkRight[man.walkcount//3], (man.x,man.y))
                man.walkcount += 1

        else:
            if man.left:
                win.blit(walkLeft[0], (man.x, man.y))

            elif man.right:
                    win.blit(walkRight[0], (man.x, man.y))

            else:
                win.blit(char, (man.x,man.y))

        self.box = (self.x + 16, self.y + 12, 32, 48)
        #pygame.draw.rect(win, (255, 0, 0), self.box, 2)

    def hit(self):
        self.x = 40
        self.y = 400
        self.Jumpcount = 6
        self.isJump = False
        self.walkcount = 0

class enemy(object):
    def __init__(self, x,y, height, width, end):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.end = end
        self.vel = 8
        self.direction = 1
        self.left = False
        self.right = True
        self.path = (self.x, self.end)
        self.walkcount = 0
        self.box = (self.x + 14, self.y + 5, 34, 50)
        self.health = 10
        self.visible = True

    def run(self, win):
        self.x += self.vel*self.direction
        self.walkcount += 1

        if self.x > self.path[1] or self.x <= self.path[0]:
            self.direction *= -1
            self.walkcount = 1
            self.x += self.vel*self.direction

            if self.direction == 1:
                self.right = True
                self.left = False

            else:
                self.right = False
                self.left = True

        if self.right:
            win.blit(EwalkRight[self.walkcount//11], (self.x, self.y))

        elif self.left:
            win.blit(EwalkLeft[self.walkcount//11], (self.x, self.y))

        pygame.draw.rect(win, (255, 0, 0), (self.box[0] - 10, self.box[1] - 20, 40, 10))
        pygame.draw.rect(win, (0, 150, 0), (self.box[0] - 10, self.box[1] - 20, 4*(self.health), 10))
        self.box = (self.x + 14, self.y + 5, 34, 50)
        #pygame.draw.rect(win, (255, 0, 0), self.box, 2)

    def hit(self):
        print("HITTTTT!!!!!!!!")
        self.health -= 1


class projectile(object):
    def __init__(self,x,y,radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20*facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def renderscreen():
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (370, 10))
    man.draw(win)
    if villian.health > 0:
        villian.run(win)
    
    else:
        villian.visible = False

    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
font1 = pygame.font.SysFont('comicsans', 100)
villian = enemy(100, 400, 64, 64, 300)
man = player(40,400,64, 64)
bullets = []
bulletcount = 5
run = True
while run:
    pygame.time.delay(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if man.box[1] < villian.box[1] + villian.box[3] and \
      man.box[1] + man.box[3] > villian.box[1]:
        if man.box[0] < villian.box[0] + villian.box[2] and \
          man.box[0] + man.box[2] > villian.box[0]:
            score -= 5
            man.hit()
            text2 = font1.render("-5",1, (255, 0, 0))
            win.blit(text2, ((screen_width - text2.get_width())/2, screen_height/2))
            pygame.display.update()
            i = 0
            while i < 300:
                pygame.time.delay(10)
                i += 1

                keys = pygame.key.get_pressed()

                for key in keys:
                    if key == pygame.QUIT:
                        quit

    
    
    for bullet in bullets:

        bullet.x += bullet.vel
        if bullet.x >= 500 or bullet.x <= 0:
            bullets.remove(bullet)
            bulletcount += 1
            continue

        if villian.visible:
            if bullet.y - bullet.radius < villian.box[1] + villian.box[3] and \
              bullet.y + bullet.radius > villian.box[1]:
                if bullet.x > villian.box[0] and bullet.x < villian.box[0] + villian.box[2]:
                    hitsound.play()
                    villian.hit()
                    bullets.remove(bullet)
                    bulletcount += 1
                    score += 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and bulletcount > 0:
        bulletsound.play()
        if man.right:
            facing = 1
        else: facing = -1
        newbullet = projectile(man.x + 32, man.y+ 32, 5, (255, 255, 255), facing)
        bullets.append(newbullet)
        bulletcount -= 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.right = False
        man.left = True
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.vel - man.width :
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False

    else:
        man.standing = True
        man.walkcount = 0
    #     man.right = False
    #     man.left = False

    if not (man.isJump):
        # if keys[pygame.K_UP] and man.y> man.vel:
        #     man.y -= man.vel
        #
        # if keys[pygame.K_DOWN] and man.y < screen_height - man.vel - man.height:
        #     man.y += man.vel

        if keys[pygame.K_UP]:
            man.isJump = True

    else:

        if man.Jumpcount >= -6:
            neg = 1
            if man.Jumpcount < 0:
                neg = -1

            man.y -= (man.Jumpcount**2) * neg
            man.Jumpcount -= 1

        else:
            man.isJump = False
            man.Jumpcount = 6

    renderscreen()



pygame.quit()
