import pygame
import logging

class PlayingField(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)