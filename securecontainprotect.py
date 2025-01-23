import pygame
import traceback
import logging
import pyautogui
from cards import *

pygame.init()
logger = logging.getLogger(__name__)
clock = pygame.time.Clock()

clientNumber = 0

def redraw_window(window: pygame.Surface, card: Card = None, deck = None, player = None):
    window.fill((100, 100, 255))
    if card != None:
        card.draw(window)
    if deck != None:
        for card in deck:
            card.draw(window)
    pygame.display.update()

def main():
    logging.basicConfig(filename='scpgame.log', level=logging.INFO)
    logger.info("Started...")
    running = True

    info = pygame.display.Info()
    width, height = info.current_w, info.current_h
    pygame.display.set_caption("Client")
    fullscreen = False
    window = pygame.display.set_mode((width, height))

    deck = [Card("DEFAULT", 50, 50, "temporarycardsprite.png") for i in range(52)]
    for card in deck:
        card.scale(20, 2)
    held_card_i = None

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
                    for num, obj in enumerate(deck):
                        if obj.get_internal_rect().collidepoint(event.pos) and obj.is_draggable:
                            held_card_i = num

            if event.type == pygame.MOUSEMOTION: # Drag the currently held card
                if held_card_i != None:
                    deck[held_card_i].get_internal_rect().move_ip(event.rel)

            if event.type == pygame.MOUSEBUTTONUP: # Stop Dragging a card
                if event.button == 1:
                    held_card_i = None

            if event.type == pygame.QUIT:
                running = False
                
        redraw_window(window, deck= deck)
        clock.tick(60)
    pygame.quit()
    logger.info(f"Finished at time: {clock.get_time()}")

if __name__ == "__main__":
    main()