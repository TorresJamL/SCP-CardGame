import pygame
import logging
import os
from cards import Card
from sprites import *
logger = logging.getLogger(__name__)

#TODO: Make a Card Container class to hold cards both internally and visually.
class CardContainer(Sprite):
    """
    Container for cards to lock into when placed. 
    """
    def __init__(self, x:int, y:int, card_limit:int, image_name:str = "tempcontainer.png", *groups):
        super().__init__(x, y, image_name, *groups)
        self.card_limit = card_limit
        self.__cards_contained = {}
    
    def get_contained_cards(self):
        return self.__cards_contained
    
    def remove_card(self, card_id:int):
        if card_id == None:
            raise ValueError("None entered as an argument... why")  
        elif type(card_id) != int:
            raise ValueError(f"Incorrect Value Entered: {card_id}. Type 'int' was expected")
        else:
            card = self.__cards_contained.pop(card_id)
            return card
        
    def contain_card(self, card: Card):
        if type(card) != Card:
            raise ValueError(f"Type: Card, was expected. Recieved: {type(card)}")
        elif len(self.__cards_contained) < self.card_limit:
            card.get_internal_rect().topleft = (self.rect.topleft[0], self.rect.topleft[1])
            self.__cards_contained[card.get_ID()] = card
        else:
            print("Card Limit exceeded, input declined.")

class PlayingField(pygame.sprite.Sprite):
    """The playing field consists of 3 notable areas:
        - The center where most cards will be played against each other.
        - The "bench" where cards meant to "support" will be.
        - The player decks, where the players get cards from.
        NOTE: Keep Within MVP scope
    """
    def __init__(self, image_name, *groups):
        super().__init__(*groups)
        #RE-EVALUTATE
        image_path = os.path.join("assets", image_name)
        self.__in_play_cards_p1:list[Card] = []
        self.__in_play_cards_p2:list[Card] = []
        self.__benched_cards:list[Card] = []

    def get_cards_in_play(self)->tuple[list[Card], list[Card]]:
        """Returns a tuple of lists of all cards on the playing field
        
        Returns:
            tuple[list[Card], list[Card]]: A tuple with the 0th index being the first player's card, and the 1st index being the second player's card. 
        """
        #NOTE: Update to match the re-evalution of the class
        return self.__in_play_cards_p1, self.__in_play_cards_p2