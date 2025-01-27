import pygame
import logging
import os
from sprites import *
logger = logging.getLogger(__name__)

clock = pygame.time.Clock()

class Card(Sprite):
    def __init__(self, name:str, id:int, x:int, y:int, image_name:str, tags:list[str] = ['card'], *groups):
        super().__init__(x, y, image_name, *groups)
        self.is_draggable = True
        self.name = name
        self.__tags = tags
        self.__id = id
        logger.info(f"Card Created: {self}; Image: {self.image}, {self.image_path}; Time: {clock.get_time()}")

    def get_tags(self):
        return self.__tags

    def get_ID(self):
        return self.__id

    def add_tag(self, tag:str):
        self.__tags.append(tag)

    def remove_tag(self, tag:str):
        if tag in self.__tags:
            self.__tags.remove(tag)
    
    def scale(self, scale_x:float, scale_y:float):
        pygame.transform.scale(self.image, (scale_x, scale_y))

    def __str__(self):
        return f"Name: {self.name}\nID: {self.__id}\nTags: {self.__tags}"
    
    def __repr__(self):
        return ""

