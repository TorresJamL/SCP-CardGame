import pygame 
import os
import logging
logger = logging.getLogger(__name__)

class Sprite(pygame.sprite.Sprite):
    """General Sprite class for all displayed sprites.
    """
    def __init__(self, x:int, y:int, image_name:str, *groups):
        super().__init__(*groups)
        self.image_path = os.path.join("assets", image_name)
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def get_pos(self):
        """Returns the coords of the top left of the internal rectangle.

        Returns:
            Tuple[int, int]: A tuple containing the x and y
        """
        return self.rect.topleft

    def get_internal_rect(self)->pygame.Rect:
        """Returns the internal rectangle of the image.
        
        Returns:
            pygame.Rect
        """
        return self.rect
        
    def draw(self, window: pygame.Surface):
        window.blit(self.image, self.rect.topleft)
        
    def update(self):
        logger.info(f"Update Occured: {self}")
        super().update()
    