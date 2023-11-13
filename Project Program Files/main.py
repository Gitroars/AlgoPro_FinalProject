
import pygame, sys,os

import string

from ships import Player
from letterTile import *



class Game:



    def __init__(self):
        self.game_over = False
        #Background setup
        blueBackground = pygame.image.load("Backgrounds/blue.png")
        darkPurpleBackground = pygame.image.load("Backgrounds/darkPurple.png")
        self.bluebg = pygame.transform.scale(blueBackground, (1280, 720))
        self.dpbg = pygame.transform.scale(darkPurpleBackground,(1280,720))
        # Player setup
        playerSprite = Player((screen_width / 2, screen_height - 50), screen_width, 7.5)
        self.player = pygame.sprite.GroupSingle(playerSprite)
        #Word setup
        self.word_ready = True
        #Tile Setup
        self.tile_ready = True
        self.tile_time = 0
        self.tile_cooldown = 1500
        # Tile Sprite Group Setup
        self.tiles = pygame.sprite.Group()
        self.tilesA = pygame.sprite.Group()
        self.tilesB = pygame.sprite.Group()
        self.tilesC = pygame.sprite.Group()
        self.tilesD = pygame.sprite.Group()
        self.tilesE = pygame.sprite.Group()
        self.tilesF = pygame.sprite.Group()
        self.tilesG = pygame.sprite.Group()
        self.tilesH = pygame.sprite.Group()
        self.tilesI = pygame.sprite.Group()
        self.tilesJ = pygame.sprite.Group()
        self.tilesK = pygame.sprite.Group()
        self.tilesL = pygame.sprite.Group()
        self.tilesM = pygame.sprite.Group()
        self.tilesN = pygame.sprite.Group()
        self.tilesO = pygame.sprite.Group()
        self.tilesP = pygame.sprite.Group()
        self.tilesQ = pygame.sprite.Group()
        self.tilesR = pygame.sprite.Group()
        self.tilesS = pygame.sprite.Group()
        self.tilesT = pygame.sprite.Group()
        self.tilesU = pygame.sprite.Group()
        self.tilesV = pygame.sprite.Group()
        self.tilesW = pygame.sprite.Group()
        self.tilesX = pygame.sprite.Group()
        self.tilesY = pygame.sprite.Group()
        self.tilesZ = pygame.sprite.Group()
        # Health and Score setup
        self.myfont = pygame.font.SysFont("arial", 50)
        self.heartImg = pygame.image.load("PNG/UI/heart.png")
        self.life = 3
        self.score = 0
        # Background Music Setup
        self.musics = []
        for file in os.listdir("BGM"): #Loop through BGM directory and add all files inside to a music list
            self.musics.append(file)
        self.playMusic()
        # Correct Tile Collection Sound Effect
        self.correct_sound = pygame.mixer.Sound("SFX/sfx_zap.ogg")
        self.correct_sound.set_volume(0.4)
        # Explosion Sound Effect
        self.explosion_sound = pygame.mixer.Sound("SFX/mixkit-shatter-shot-explosion-1693.wav")
        self.explosion_sound.set_volume(0.1)
        # Game Over Sound
        self.lose_sound = pygame.mixer.Sound("SFX/sfx_lose.ogg")
        self.lose_sound.set_volume(0.5)


    def display_score(self):
        self.scoreText = self.myfont.render(str(self.score),True,(255,255,255))
        screen.blit(self.scoreText,(0,50))
    def display_life(self):
        self.lifeText = self.myfont.render(str(self.life),True,(255,255,255))
        screen.blit(self.heartImg,(screen_width-200,50))
        screen.blit(self.lifeText,(screen_width-100,75))
    def display_target(self):
        distance = 0 #between rows
        distanceCharNum = 35 #between columns
        distanceScoreCharNum = 100 #to be away from the score text
        for char in self.lettersChar:
            distance += 40
            screen.blit(self.myfont.render(char, True, (255, 255, 0)), (0, distanceScoreCharNum + distance))
        distance = 0
        for num in self.currentNum:
            distance += 40
            screen.blit(self.myfont.render(str(num) + "/", True, (255, 255, 255)),
                        (distanceCharNum, distanceScoreCharNum + distance))
        distance = 0
        for num in self.lettersNum:
            distance += 40
            screen.blit(self.myfont.render(str(num), True, (255, 255, 255)),
                        (distanceCharNum * 2, distanceScoreCharNum + distance))
        screen.blit(self.randomText, (0, 0))

    def generate_word(self):
        if self.word_ready:
         self.textFile = open("data.txt","r")
         self.content = str(self.textFile.read())
         #Reference: https://datagy.io/python-remove-punctuation-from-string/#Use_Python_to_Remove_Punctuation_from_a_String_with_Translate
         self.newContent = self.content.translate(str.maketrans('','',string.punctuation))

         self.textList = self.newContent.split() #Convert to list type
         self.randomWord = random.choice(self.textList).upper() #Chooses a random word from the list with uppercase form
         self.letters = {} #Initialize a dictionary for amount of characters

         for char in self.randomWord:
             self.letters[char] = self.letters.get(char,0)+1 #Create a key-value(letter-amount of said letter) from selected word

         self.lettersChar = sorted(self.letters.keys()) #an alphabetically ordered list
         self.lettersNum = [] #the value list for ordered letter list
         for char in self.lettersChar:
             self.lettersNum.append(self.letters.get(char))

         self.currentNum = self.lettersNum.copy()
         for i in range(len(self.currentNum)):
             self.currentNum[i] = 0

         self.randomText = self.myfont.render(self.randomWord, True, (255, 255, 0))
         self.word_ready = False

        else:
            self.display_target()

    def generate_tile(self):
         if self.tile_ready:
           randomInt = random.randrange(len(LetterTile.subclasses))
           # Creates a tile object on the letter group, and add the corresponding group to the main tile group
           if randomInt == 0:
               self.tilesA.add(LetterA())
               self.tiles.add(self.tilesA)
           elif randomInt == 1:
               self.tilesB.add(LetterB())
               self.tiles.add(self.tilesB)
           elif randomInt == 2:
               self.tilesC.add(LetterC())
               self.tiles.add(self.tilesC)
           elif randomInt == 3:
               self.tilesD.add(LetterD())
               self.tiles.add(self.tilesD)
           elif randomInt == 4:
               self.tilesE.add(LetterE())
               self.tiles.add(self.tilesE)
           elif randomInt == 5:
               self.tilesF.add(LetterF())
               self.tiles.add(self.tilesF)
           elif randomInt == 6:
               self.tilesG.add(LetterG())
               self.tiles.add(self.tilesG)
           elif randomInt == 7:
               self.tilesH.add(LetterH())
               self.tiles.add(self.tilesH)
           elif randomInt == 8:
               self.tilesI.add(LetterI())
               self.tiles.add(self.tilesI)
           elif randomInt == 9:
               self.tilesJ.add(LetterJ())
               self.tiles.add(self.tilesJ)
           elif randomInt == 10:
               self.tilesK.add(LetterK())
               self.tiles.add(self.tilesK)
           elif randomInt == 11:
               self.tilesL.add(LetterL())
               self.tiles.add(self.tilesL)
           elif randomInt == 12:
               self.tilesM.add(LetterM())
               self.tiles.add(self.tilesM)
           elif randomInt == 13:
               self.tilesN.add(LetterN())
               self.tiles.add(self.tilesN)
           elif randomInt == 14:
               self.tilesO.add(LetterO())
               self.tiles.add(self.tilesO)
           elif randomInt == 15:
               self.tilesP.add(LetterP())
               self.tiles.add(self.tilesP)
           elif randomInt == 16:
               self.tilesQ.add(LetterQ())
               self.tiles.add(self.tilesQ)
           elif randomInt == 17:
               self.tilesR.add(LetterR())
               self.tiles.add(self.tilesR)
           elif randomInt == 18:
               self.tilesS.add(LetterS())
               self.tiles.add(self.tilesS)
           elif randomInt == 19:
               self.tilesT.add(LetterT())
               self.tiles.add(self.tilesT)
           elif randomInt == 20:
               self.tilesU.add(LetterU())
               self.tiles.add(self.tilesU)
           elif randomInt == 21:
               self.tilesV.add(LetterV())
               self.tiles.add(self.tilesV)
           elif randomInt == 22:
               self.tilesW.add(LetterW())
               self.tiles.add(self.tilesW)
           elif randomInt == 23:
               self.tilesX.add(LetterX())
               self.tiles.add(self.tilesX)
           elif randomInt == 24:
               self.tilesY.add(LetterY())
               self.tiles.add(self.tilesY)
           elif randomInt == 25:
               self.tilesZ.add(LetterZ())
               self.tiles.add(self.tilesZ)
           self.tile_ready = False
           self.tile_time = pygame.time.get_ticks()
         elif not self.tile_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.tile_time >= self.tile_cooldown:
                self.tile_ready = True

    def goodShipCollide(self):

        index = self.lettersChar.index(self.collidedLetter)
        currentNumIndex = self.currentNum[index]
        maxNumIndex = self.lettersNum[index]


        if currentNumIndex < maxNumIndex: #Adds a point to list of current amount of collided letter, with condition still below the required amount for said letter
            self.currentNum[index] += 1
            self.score += 100
            self.correct_sound.play()
        elif currentNumIndex >= maxNumIndex:
            self.badCollide()

        totalNum = len(self.lettersNum)

        finishedNum = 0
        for i in range(totalNum): #For every number,
            if self.currentNum[i]==self.lettersNum[i]: #Check if the current collected amount of a letter matches with the required amount of a letter
                finishedNum += 1 #Upon a match, then increase the completion index by 1

            if finishedNum == totalNum: #Once all the required amount of letters are collected, which is determined by a match between completion index and length of number list
                self.word_ready = True #choose a new random word

    #Scorepoints and SFX upon laser collission
    def goodLaserCollide(self):
        self.score += 10
        self.explosion_sound.play()
    #Penalties and SFX upon physical collisison
    def badCollide(self):
        self.life -=1
        if self.life == 0:
            self.endGame()
        self.explosion_sound.play()
    #Play random music endlessly(a random one once current music is over)
    def playMusic(self):
        randomMusic = random.choice(self.musics)
        currentMusic = pygame.mixer.Sound("BGM/"+randomMusic)
        currentMusic.set_volume(0.2)
        currentMusic.play()



    #Checks if a tile is hit by a laser
    def checkCollisionBetweenTileAndLaser(self):
        if pygame.sprite.groupcollide(self.tiles, self.player.sprite.lasers, True, True):
            self.goodLaserCollide()



    #Checks if a tile collided with the spaceship
    def checkCollissionBetweenTileAndPlayer(self):
        stateCollided = False
        self.collidedLetter = ""
        if pygame.sprite.groupcollide(self.tilesA,self.player,True,False):
            self.collidedLetter = "A"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesB, self.player, True,False):
            self.collidedLetter = "B"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesC, self.player, True,False):
            self.collidedLetter = "C"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesD, self.player, True, False):
            self.collidedLetter = "D"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesE, self.player, True, False):
            self.collidedLetter = "E"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesF, self.player, True, False):
            self.collidedLetter = "F"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesG, self.player, True, False):
            self.collidedLetter = "G"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesH, self.player, True, False):
            self.collidedLetter = "H"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesI, self.player, True, False):
            self.collidedLetter = "I"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesJ, self.player, True, False):
            self.collidedLetter = "J"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesK, self.player, True, False):
            self.collidedLetter = "K"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesL, self.player, True, False):
            self.collidedLetter = "L"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesM, self.player, True, False):
            self.collidedLetter = "M"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesN, self.player, True, False):
            self.collidedLetter = "N"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesO, self.player, True, False):
            self.collidedLetter = "O"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesP, self.player, True, False):
            self.collidedLetter = "P"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesQ, self.player, True, False):
            self.collidedLetter = "Q"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesR, self.player, True, False):
            self.collidedLetter = "R"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesS, self.player, True, False):
            self.collidedLetter = "S"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesT, self.player, True, False):
            self.collidedLetter = "T"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesU, self.player, True, False):
            self.collidedLetter = "U"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesV, self.player, True, False):
            self.collidedLetter = "V"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesW, self.player, True, False):
            self.collidedLetter = "W"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesX, self.player, True, False):
            self.collidedLetter = "X"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesY, self.player, True, False):
            self.collidedLetter = "Y"
            stateCollided = True

        if pygame.sprite.groupcollide(self.tilesZ, self.player, True, False):
            self.collidedLetter = "Z"
            stateCollided = True
        if stateCollided:
         if self.collidedLetter in self.letters :
            self.goodShipCollide()
         else:
            self.badCollide()
         stateCollided = False

    def checkMusicPlaying(self):
        if pygame.mixer.get_busy() == False:
            print('get new song')
            self.playMusic()

    #Put background on screen
    def background(self):
        screen.blit(self.bluebg, (0, 0))

    def run(self):
      if self.game_over == False:

         #Background Update
         self.background()
         #Interface Update
         self.display_score()
         self.display_life()
         self.generate_word()
         #Player Movement
         self.player.update()
         self.player.sprite.lasers.draw(screen)
         self.player.draw(screen)
         #Tile Instances
         self.generate_tile()
         #Letter Tiles Movement
         self.tiles.update()
         self.tiles.draw(screen)
         #Collission check
         self.checkCollissionBetweenTileAndPlayer()
         self.checkCollisionBetweenTileAndLaser()
        #Check if music stream is playing
         self.checkMusicPlaying()


    def endGame(self):
        self.game_over = True
        self.lose_sound.play()
        endText = self.myfont.render("GAME OVER",True,(200,200,200))
        scoreText = self.myfont.render("Score: "+str(self.score),True,(255,255,255))
        screen.blit(self.dpbg,(0,0)) #Change background to dark purple
        screen.blit(endText,(screen_width/2 ,screen_height/2 )) #Shows that the game is over
        screen.blit(scoreText,(screen_width/2,screen_height/2+100)) #displays the session's score

if __name__ == '__main__':
    pygame.init()
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Word Box Juice")
    gameIcon = pygame.image.load('PNG/ufoRed.png')
    pygame.display.set_icon(gameIcon)
    clock = pygame.time.Clock() #Object to keep track of time
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game.run()
        pygame.display.flip() #Update entire display screen
        clock.tick(60) #Framerate is at 60fps

