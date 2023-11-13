import random
import pygame


class LetterTile(pygame.sprite.Sprite):
    subclasses = []
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('PNG/Box/rsz_letter.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(int(1280/3),int(1280/3)*2-self.rect.width)
        self.rect.y = random.randrange(0,int(720/10-self.rect.height))
        self.height_y_constraint = 600
        self.speed = 3

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint:
            self.kill()





    def update(self):
        self.rect.y += self.speed
        self.destroy()



#LETTER TILE VARIANTS - subclasses
class LetterA(LetterTile):

    def __init__(self):
        super(LetterA, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_A.png').convert_alpha()


class LetterB(LetterTile):
    def __init__(self):
        super(LetterB, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_B.png').convert_alpha()


class LetterC(LetterTile):
    def __init__(self):
        super(LetterC, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_C.png').convert_alpha()


class LetterD(LetterTile):
    def __init__(self):
        super(LetterD, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_D.png').convert_alpha()


class LetterE(LetterTile):
    def __init__(self):
        super(LetterE, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_E.png').convert_alpha()


class LetterF(LetterTile):
    def __init__(self):
        super(LetterF, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_F.png').convert_alpha()


class LetterG(LetterTile):
    def __init__(self):
        super(LetterG, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_G.png').convert_alpha()


class LetterH(LetterTile):
    def __init__(self):
        super(LetterH, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_H.png').convert_alpha()


class LetterI(LetterTile):
    def __init__(self):
        super(LetterI, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_I.png').convert_alpha()


class LetterJ(LetterTile):
    def __init__(self):
        super(LetterJ, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_J.png').convert_alpha()


class LetterK(LetterTile):
    def __init__(self):
        super(LetterK, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_K.png').convert_alpha()


class LetterL(LetterTile):
    def __init__(self):
        super(LetterL, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_L.png').convert_alpha()


class LetterM(LetterTile):
    def __init__(self):
        super(LetterM, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_M.png').convert_alpha()


class LetterN(LetterTile):
    def __init__(self):
        super(LetterN, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_N.png').convert_alpha()


class LetterO(LetterTile):
    def __init__(self):
        super(LetterO, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_O.png').convert_alpha()


class LetterP(LetterTile):
    def __init__(self):
        super(LetterP, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_P.png').convert_alpha()


class LetterQ(LetterTile):
    def __init__(self):
        super(LetterQ, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_Q.png').convert_alpha()


class LetterR(LetterTile):
    def __init__(self):
        super(LetterR, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_R.png').convert_alpha()


class LetterS(LetterTile):
    def __init__(self):
        super(LetterS, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_S.png').convert_alpha()


class LetterT(LetterTile):
    def __init__(self):
        super(LetterT, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_T.png').convert_alpha()


class LetterU(LetterTile):
    def __init__(self):
        super(LetterU, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_U.png').convert_alpha()


class LetterV(LetterTile):
    def __init__(self):
        super(LetterV, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_V.png').convert_alpha()


class LetterW(LetterTile):
    def __init__(self):
        super(LetterW, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_W.png').convert_alpha()


class LetterX(LetterTile):
    def __init__(self):
        super(LetterX, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_X.png').convert_alpha()


class LetterY(LetterTile):
    def __init__(self):
        super(LetterY, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_Y.png').convert_alpha()


class LetterZ(LetterTile):
    def __init__(self):
        super(LetterZ, self).__init__()
        self.image = pygame.image.load('PNG/Box/letter_Z.png').convert_alpha()
