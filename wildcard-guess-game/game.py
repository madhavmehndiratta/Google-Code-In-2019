import pygame
import time
import random

pygame.init()
gameDisplay = pygame.display.set_mode([800,600])
pygame.display.set_caption("Wildcard Guess Game")

clock = pygame.time.Clock()
FPS = 15

purple = (102,53,153)
white = (255, 255, 255)
black = (0, 0, 0)
red = (210, 35, 42)
light_blue = (31, 216, 230)
blue = (40, 53, 88)
yellow = (255, 255, 0)
green = (0, 150, 0)
light_yellow = (200, 200, 0)
light_red = (150, 0, 0)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


inputText = pygame.image.load("resources/input.png") 

global BackGround
BackGround = Background('resources/start_background.png', [-300,-300])

global fedora
fedora = pygame.image.load("resources/fedora.png")
fedora = pygame.transform.scale(fedora, (200, 200))

global metasploit
metasploit = pygame.image.load("resources/metasploit.png")
metasploit = pygame.transform.scale(metasploit, (200, 200))

global gucci
gucci = pygame.image.load("resources/gucci.jpg")
gucci = pygame.transform.scale(gucci, (300, 200))

global bentley
bentley = pygame.image.load("resources/bentley.jpg")
bentley = pygame.transform.scale(bentley, (300, 200))

global gtr
gtr = pygame.image.load("resources/gtr.jpg")
gtr = pygame.transform.scale(gtr, (300, 200))

global parrot
parrot = pygame.image.load("resources/parrot.png")
parrot = pygame.transform.scale(parrot, (200, 200))

global keylogger
keylogger = pygame.image.load("resources/keylogger.jpg")
keylogger = pygame.transform.scale(keylogger, (200, 200))

global centos
centos = pygame.image.load("resources/centos.png")
centos = pygame.transform.scale(centos, (200, 200))

global lubuntu
lubuntu = pygame.image.load("resources/lubuntu.png")
lubuntu = pygame.transform.scale(lubuntu, (300, 300))

global xubuntu
xubuntu = pygame.image.load("resources/xubuntu.png")
xubuntu = pygame.transform.scale(xubuntu, (200, 200))

wordGuessFont = pygame.font.SysFont("CopperPlate Gothic", 50)   
wordType = pygame.font.SysFont("Calibri", 50)                   
scoreFont = pygame.font.SysFont("Comic Sans MS", 30)           
hintFont = pygame.font.SysFont("Comic Sans MS", 20)             
infoFont = hintFont = pygame.font.SysFont("Comic Sans MS", 30)
helpFont = pygame.font.SysFont("Comic Sans MS", 25)            
startFont = pygame.font.SysFont("Comic Sans MS", 35)        
msgFont = pygame.font.SysFont("CopperPlate Gothic",25) 
congoFont = pygame.font.SysFont("CopperPlate Gothic", 50)  
answerFont = pygame.font.SysFont("Juice ITC", 50)     
       
def DrawRoundRect(gameDisplay, color, rect, width, xr, yr):
    clip = gameDisplay.get_clip()
    
    gameDisplay.set_clip(clip.clip(rect.inflate(0, -yr*2)))
    pygame.draw.rect(gameDisplay, color, rect.inflate(1-width,0), width)

    gameDisplay.set_clip(clip.clip(rect.inflate(-xr*2, 0)))
    pygame.draw.rect(gameDisplay, color, rect.inflate(0,1-width), width)

    gameDisplay.set_clip(clip.clip(rect.left, rect.top, xr, yr))
    pygame.draw.ellipse(gameDisplay, color, pygame.Rect(rect.left, rect.top, 2*xr, 2*yr), width)

    gameDisplay.set_clip(clip.clip(rect.right-xr, rect.top, xr, yr))
    pygame.draw.ellipse(gameDisplay, color, pygame.Rect(rect.right-2*xr, rect.top, 2*xr, 2*yr), width)

    gameDisplay.set_clip(clip.clip(rect.left, rect.bottom-yr, xr, yr))
    pygame.draw.ellipse(gameDisplay, color, pygame.Rect(rect.left, rect.bottom-2*yr, 2*xr, 2*yr), width)

    gameDisplay.set_clip(clip.clip(rect.right-xr, rect.bottom-yr, xr, yr))
    pygame.draw.ellipse(gameDisplay, color, pygame.Rect(rect.right-2*xr, rect.bottom-2*yr, 2*xr, 2*yr), width)

    gameDisplay.set_clip(clip)

def displayPicture(level):
    if level == 1:
        gameDisplay.blit(fedora, [300,100])
        answer = "fedora"
        hint = "A famous linux distribution primarily sponsored by Red Hat Inc."

    elif level == 2:
        gameDisplay.blit(metasploit, [300,100])
        answer = "metasploit"
        hint = "A Computer security owned by company Rapid7."

    elif level == 3:
        gameDisplay.blit(gucci, [250,150])
        answer = "gucci"
        hint = "It is an Italian luxury brand of fashion and leather goods."

    elif level == 4:
        gameDisplay.blit(bentley, [250,150])
        answer = "bentley"
        hint = "A British manufacturer and marketer of luxury cars and SUVs."

    elif level == 5:
        gameDisplay.blit(gtr, [250,150])
        answer = "gtr"
        hint = "A sports car produced by Nissan, which was unveiled in 2007."

    elif level == 6:
        gameDisplay.blit(parrot, [300,100])
        answer = "parrot"
        hint = "A newly released GNU/Linux distribution based on Debian."

    elif level == 7:
        gameDisplay.blit(keylogger, [300,100])
        answer = "keylogger"
        hint = "It is a device used for keystroke logging."

    elif level == 8:
        gameDisplay.blit(centos, [300,100])
        answer = "centos"
        hint = "A Linux distribution owned by Red Hat Enterprise Linux (RHEL)."

    elif level == 9:
        gameDisplay.blit(lubuntu, [260,80])
        answer = "lubuntu"
        hint = "A flavor Ubuntu, using the LXQt desktop environment."

    elif level == 10:
        gameDisplay.blit(xubuntu, [300,100])
        answer = "xubuntu"
        hint = "A flavor of Ubuntu, using the Xfce desktop environment."
        
    return answer, hint
                                     
def displayHint(hint):
    hintText = hintFont.render("Hint: "+hint, True, blue)
    gameDisplay.blit(hintText, [30,400])

def displayScore(score):
    scoreText = scoreFont.render("Score: "+str(score), True, black)
    gameDisplay.blit(scoreText, [36,36])

def typeChar(char):
    TypeChar = wordType.render(char.upper(), True, green)
    gameDisplay.blit(TypeChar, [50,535])
    pygame.display.update()

def checkAnswer(answer, string):
    if answer == string.lower():
        msgAnswer = answerFont.render("Correct!", True, yellow)
        pygame.draw.rect(gameDisplay, green, [0,500,800,600])
        gameDisplay.blit(msgAnswer, [300,530])
        
        
    else:
        msgAnswer = answerFont.render("Sorry! The Correct Answer is "+ answer.upper(), True, yellow)
        pygame.draw.rect(gameDisplay, green, [0,500,800,600])
        gameDisplay.blit(msgAnswer, [50,530])

    pygame.display.update()
    pExit = False
    
    while not pExit:
        for event_3 in pygame.event.get():
            if event_3.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event_3.type == pygame.KEYDOWN:
                if event_3.key == pygame.K_RETURN:
                    pExit = True
                    break

def gameComplete(score):                                            
    for printRect in range(0,610,10):
        pygame.draw.rect(gameDisplay, yellow, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)

    clock.tick(1)                                                                       
    cExit = False
    if score == 0:
        msgOver = congoFont.render("GAME OVER!", True, purple)
    else:
        msgOver = congoFont.render("CONGRATULATIONS!", True, purple)
    finalScore = infoFont.render("YOUR SCORE: "+str(score), True, purple)
    playAgain = helpFont.render("PLAY AGAIN", True, black)
    quitGame = helpFont.render("QUIT", True, black)

    gameDisplay.blit(BackGround.image, BackGround.rect)           
    pygame.display.update()
    clock.tick(5)
    
    gameDisplay.blit(msgOver, [250,100])
    pygame.display.update()
    clock.tick(5)
    
    gameDisplay.blit(finalScore, [300,330])
    pygame.display.update()
    clock.tick(5)
    pygame.display.update()
    clock.tick(5)
    
    while not cExit:                                                                    
        gameDisplay.blit(BackGround.image, BackGround.rect)                                                
        gameDisplay.blit(msgOver, [250,100])
        gameDisplay.blit(finalScore, [300,330])

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 80+200 > cur[0] > 100 and 300+80 > cur[1] > 300:                             
            DrawRoundRect(gameDisplay, (light_blue), pygame.Rect(80, 300, 130, 70), 0, 27, 27)
            if click[0] == 1:
                for printRect in range(0,610,10):
                    pygame.draw.rect(gameDisplay, black, [0,600-(printRect),800,50+(printRect)])
                    pygame.display.update()
                    clock.tick(70)
                gameLoop()
        else:
            DrawRoundRect(gameDisplay, (light_blue), pygame.Rect(80, 300, 130, 70), 0, 27, 27)

        if 580+100 > cur[0] > 500 and 300+50 > cur[1] > 300:
            DrawRoundRect(gameDisplay, (red), pygame.Rect(580, 300, 130, 70), 0, 27, 27)
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            DrawRoundRect(gameDisplay, (red), pygame.Rect(580, 300, 130, 70), 0, 27, 27)

        gameDisplay.blit(playAgain, [95,325])
        gameDisplay.blit(quitGame, [620,325])

        pygame.display.update()
            
        for event_2 in pygame.event.get():
            if event_2.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
def startScreen():
    clock.tick(1)
    sExit = False
    helpLine1 = infoFont.render("* You need to guess the picture that appears on the screen", True, yellow)
    helpLine2 = infoFont.render("* You will be given 1 chance for each picture", True, yellow)
    helpLine3 = infoFont.render("* There is a time limit of 15 seconds", True, yellow)
    helpLine7 = infoFont.render("* There are 10 levels, and 1 picture per level", True, yellow)
    helpLine8 = infoFont.render("* Plus 100 points for each correct word multiplied by the level", True, yellow)
    helpLine9 = infoFont.render("* Hints will be available for each question", True, yellow)
    helpLine0 = infoFont.render("* 100 points deducted if you couldn't guess the word", True, yellow)

    quitGame = startFont.render("Quit the game", True, red)

    playGame = startFont.render("Play Game!", True, light_blue)

    button1 = helpFont.render("PLAY", True, black)
    button2 = helpFont.render("HELP", True, black)
    button3 = helpFont.render("QUIT", True, black)

    Level1Start = wordGuessFont.render("LEVEL 1", True, green)

    gameDisplay.blit(BackGround.image, BackGround.rect)                           
    pygame.display.update()
    clock.tick(1)
    
    heading = wordGuessFont.render("WILDCARD GUESS GAME", True, purple)
    gameDisplay.blit(heading, [195,90])
    pygame.display.update()
    clock.tick(1)

    while not sExit:
        gameDisplay.blit(BackGround.image, BackGround.rect)                                                                
        gameDisplay.blit(heading, [195,90])

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 100+100 > cur[0] > 100 and 200+50 > cur[1] > 200:
            DrawRoundRect(gameDisplay, (light_blue), pygame.Rect(98, 191, 100, 50), 0, 20, 20)
            gameDisplay.blit(playGame, [330,300])
            if click[0] == 1:   
                pygame.display.update()
                break
        else:
            DrawRoundRect(gameDisplay, (light_blue), pygame.Rect(98, 191, 100, 50), 0, 20, 20)

        if 350+100 > cur[0] > 350 and 200+50 > cur[1] > 200:
            DrawRoundRect(gameDisplay, (yellow), pygame.Rect(348, 191, 100, 50), 0, 20, 20)

            gameDisplay.blit(helpLine1, [50,300])
            gameDisplay.blit(helpLine2, [50,340])
            gameDisplay.blit(helpLine3, [50,380])
            gameDisplay.blit(helpLine7, [50,420])
            gameDisplay.blit(helpLine8, [50,460])
            gameDisplay.blit(helpLine9, [50,540])
            gameDisplay.blit(helpLine0, [50,500])
            
        else:
            DrawRoundRect(gameDisplay, (yellow), pygame.Rect(348, 191, 100, 50), 0, 20, 20)

        if 600+100 > cur[0] > 600 and 200+100 > cur[1] > 200:
            DrawRoundRect(gameDisplay, (red), pygame.Rect(598, 191, 100, 50), 0, 20, 20)
            gameDisplay.blit(quitGame, [300,300])
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            DrawRoundRect(gameDisplay, (red), pygame.Rect(598, 191, 100, 50), 0, 20, 20)

        gameDisplay.blit(button1, [125,205])
        gameDisplay.blit(button2, [375,205])
        gameDisplay.blit(button3, [625,205])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    for printRect in range(0,610,10):
        pygame.draw.rect(gameDisplay, yellow, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)

    gameDisplay.blit(Level1Start, [330,250])
    pygame.display.update()
    clock.tick(1)

    for printRect in range(0,610,10):
        gameDisplay.blit(Level1Start, [330,250])
        pygame.draw.rect(gameDisplay, black, [0,600-(printRect),800,50+(printRect)])
        gameDisplay.blit(BackGround.image, BackGround.rect)
        pygame.display.update()
        clock.tick(70)

    DrawRoundRect(gameDisplay, (yellow), pygame.Rect(10, 10, 150, 75), 0, 30, 30)
    DrawRoundRect(gameDisplay, (yellow), pygame.Rect(630, 10, 150, 75), 0, 30, 30)

def levelTransition(level):
    for printRect in range(0,610,10):
        pygame.draw.rect(gameDisplay, yellow, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)

    textLevelStart = wordGuessFont.render("LEVEL "+str(level), True, green)          
    gameDisplay.blit(textLevelStart, [300,250])                                     
    pygame.display.update()
    clock.tick(1)

    for printRect in range(0,610,10):
        gameDisplay.blit(textLevelStart, [300,250])
        pygame.display.update()
        clock.tick(100)

def displayTime(time):
    font = pygame.font.SysFont('Consolas', 30)
    gameDisplay.blit(font.render("Time Left: "+ str(time), True, (0, 0, 0)), (636, 36))

def gameLoop():
    startScreen()   
    gameExit = False
    string = ""          
    chances = 1       
    score = 0       
    clock = pygame.time.Clock()
    counter, time = 15, '15'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    level = 1  
    incorrect = 0            
       
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.USEREVENT: 
                counter -= 1
                time = str(counter).rjust(3)
                
                if counter == -1:
                    chances = 0

                    if chances == 0:                    
                        checkAnswer(answer,string)   
                        string = ""                  
                        chances = 1
                        level += 1
                        incorrect += 1
                        if incorrect == 3:
                            gameComplete(score)
                        if level == 11:
                            gameComplete(score)
                        clock.tick(5)
                        levelTransition(level)         
                        answer = displayPicture(level)
                        counter, time = 18, '18' 
                        score -= 100
                        if score < 0:
                            score = 0                

            if event.type == pygame.KEYDOWN:
                if len(string) < 16:
                    char = (chr(event.key))
                    string += char
                
                if event.key == pygame.K_RETURN:
                    if len(string) < 2:           
                        string = ""                    
                    else:
                        string = ""
                        chances -= 1                     

                    if string == answer:
                        score += 100
                        checkAnswer(answer,string)
                        string = ""
                        counter, time = 18, '18'
                        level += 1
                        if level == 11:
                            gameComplete(score)
                        else:
                            clock.tick(5)
                            levelTransition(level)
                                
                        
                    if chances == 0:                    
                        checkAnswer(answer,string)     
                        string = ""                   
                        chances = 1
                        level += 1
                        incorrect += 1
                        if incorrect == 3:
                            gameComplete(score)
                        if level == 11:
                            gameComplete(score)
                        clock.tick(5)
                        levelTransition(level)
                        counter, time = 18, '18'           
                        answer = displayPicture(level)  
                        score -= 100
                        if score < 0:
                            score = 0


                if event.key == pygame.K_BACKSPACE:
                    if string[-1] != chr(8):           
                        string = string[:-1]          
                    else:                              
                        string = string[:-2]       


        BackGround = Background('resources/start_background.png', [-300,-300])
        gameDisplay.blit(BackGround.image, BackGround.rect)
        DrawRoundRect(gameDisplay, (yellow), pygame.Rect(10, 10, 150, 75), 0, 30, 30)
        DrawRoundRect(gameDisplay, (yellow), pygame.Rect(630, 10, 150, 75), 0, 30, 30)
        displayScore(score)                        
        displayTime(time)                      
        answer, hint = displayPicture(level)
        displayHint(hint)        
    
        if string == answer:
            score += 100*level
            checkAnswer(answer,string)
            string = ""
            counter, time = 18, '18'
            level += 1
            if level == 11:
                gameComplete(score)
            clock.tick(5)
            levelTransition(level)

        gameDisplay.blit(inputText, [0,510])        
        typeChar(string)                           
        clock.tick(FPS)                            
        pygame.display.update()                     

    pygame.quit()
    quit()

gameLoop()
