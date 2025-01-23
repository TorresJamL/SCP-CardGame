import pygame
import logging
import os
logger = logging.getLogger(__name__)

clock = pygame.time.Clock()

class Card(pygame.sprite.Sprite):
    def __init__(self, name:str, x:int, y:int, image_name:str, tags:list[str] = ['card']):
        super().__init__()
        image_path = os.path.join("assets", image_name)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.is_draggable = True
        self.__tags = tags
        logger.info(f"Card Created: {self}; Image: {self.image}, {image_path}; Time: {clock.get_time()}")

    def get_pos(self):
        """Returns the coords of the top left of the internal rectangle.

        Returns:
            Tuple[int, int]: A tuple containing the x and y
        """
        return self.rect.topleft

    def get_internal_rect(self):
        return self.rect

    def get_tags(self):
        return self.__tags

    def add_tag(self, tag:str):
        self.__tags.append(tag)

    def remove_tag(self, tag:str):
        if tag in self.__tags:
            self.__tags.remove(tag)
    
    def scale(self, scale_x:float, scale_y:float):
        pygame.transform.scale(self.image, (scale_x, scale_y))

    def draw(self, window: pygame.Surface):
        window.blit(self.image, self.rect.topleft)

    def update(self):
        logger.info(f"Update Occured: {self.image}")
        super().update()
    
    def __str__(self):
        return ""
    
    def __repr__(self):
        return ""

