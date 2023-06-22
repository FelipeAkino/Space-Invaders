import pygame,os,sys


class Nave(pygame.sprite.Sprite):
    def __init__(self,groups) -> None:
        super().__init__(groups)
        self.__image = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
        self.__image = pygame.transform.scale(self.__image,(45,40))
        self.image = self.__image
        self.__rect = self.image.get_rect(center=(1200/2, 650/2))
        self.rect = self.__rect
        #Criando um timer para o disparo
        self.__pode_disparar = True
        self.__time_tiro = None
        #Implementando mascara
        self.mascara = pygame.mask.from_surface(self.image)
        #sound
        #self.som.lase = pygame.mixer.Sound(os.path.join("assets","sound","laser.ogg"))

    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def update(self):
        self.input_position()