import pygame
import traceback
import logging
import pyautogui
from cards import *
from playingfield import *

pygame.init()
logger = logging.getLogger(__name__)
clock = pygame.time.Clock()

clientNumber = 0

def initalize_game_layout():
    """Function that initializes how the actual game layout looks
    """
    # TODO: Figure something out
    #* 

    pass

def main_menu():
    pass

#TODO: DUDE, why. Make a group of every sprite or surface in the game so this function doesn't get anymore parameters.
# I'll do it later...
# Okay
# ...
# Nah
# What if... and hear me out... I did it later.
# I actually did it. I'm the coolest iteration of Jamil
def redraw_window(window:pygame.Surface, layer_manager:pygame.sprite.LayeredUpdates):
    window.fill((100, 100, 255))
    layer_manager.draw(window)
    # if card != None:
    #     card.draw(window)
    # if deck != None:
    #     for card in deck:
    #         card.draw(window)
    # if container != None:
    #     container.draw(window)
    pygame.display.update()

def main():
    logging.basicConfig(filename='scpgame.log', level=logging.INFO)
    logger.info("Started...")

    running = True
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h
    pygame.display.set_caption("Client")
    fullscreen = True
    window = pygame.display.set_mode((width, height))

    # On an object being clicked, it should be forced to the top of the layer manager.
    layer_manager = pygame.sprite.LayeredUpdates()
    test_container = CardContainer(500, 500, 1, "tempcontainer.png")
    #deck = [Card("DEFAULT", i, 50, 50, "temporarycardsprite.png") for i in range(52)]
    held_card:Card = None

    layer_manager.add(test_container)
    for i in range(52):
        layer_manager.add(Card("Default", i+1, 50, 50, "tempcard.png"))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pygame.display.set_mode((width, height), pygame.NOFRAME)
                    else:
                        window = pygame.display.set_mode((800, 600))

            if event.type == pygame.MOUSEBUTTONDOWN: # Start dragging a card
                if event.button == 1:
                    for num, obj in enumerate(layer_manager):
                        try:
                            if obj.get_internal_rect().collidepoint(event.pos) and obj.is_draggable:
                                held_card = layer_manager.get_sprite(num)
                                layer_manager.move_to_front(held_card)

                                if held_card.get_ID() in test_container.get_contained_cards():
                                    test_container.remove_card(held_card.get_ID())

                        except Exception as error:
                            logger.warning(f"Error Occured ln70: {error}\nObject might have no attribute \"is_draggable\"")

            if event.type == pygame.MOUSEMOTION: # Drag the currently held card
                if held_card != None:
                    held_card.get_internal_rect().move_ip(event.rel)
                    
            if event.type == pygame.MOUSEBUTTONUP: # Stop Dragging a card
                if event.button == 1:
                    if test_container.get_internal_rect().collidepoint(event.pos) and held_card != None and type(held_card) == Card:
                        test_container.contain_card(held_card)
                        layer_manager.move_to_front(held_card)
                    held_card = None

            if event.type == pygame.QUIT:
                running = False
                
        redraw_window(window, layer_manager)
        clock.tick(60)
    pygame.quit()
    logger.info(f"Finished at time: {clock.get_time()}")

if __name__ == "__main__":
    main()