# Author: Filippo Pisello
from chance import COMMUNITY_CHEST_LIST, CHANCE_LIST
import random

chance_list2, community_chest_list2 = CHANCE_LIST.copy(), COMMUNITY_CHEST_LIST.copy()

class Space:
    """
    Class to capture the different spaces making up the monopoly board game
    """
    def __init__(self, position: int, type_:str, color=None):
        self.position = position
        self.type = type_
        self.color = color
        self.stops = 0

    def apply_effect(self, player_obj):
        if self.type == "To jail":
            player_obj.to_jail()
        if self.type == "Chance":
            self.cards(player_obj, chance_list2, CHANCE_LIST)
        if self.type == "Community Chest":
            self.cards(player_obj, community_chest_list2, COMMUNITY_CHEST_LIST)
        return

    @staticmethod
    def cards(player_obj, cards_list, original_card_list):
        """
        Draws a random card (chance/community chest) from a set and applies its
        effect to player
        """
        if not cards_list:
            cards_list = original_card_list.copy()
        card = random.choice(cards_list)
        cards_list.remove(card)
        card.apply_effect(player_obj)
        return

# Create a list of the cells in the board
SPACE_LIST = open("Cells.txt", "r").read()
SPACE_LIST = SPACE_LIST.split("||")[1:]
SPACE_LIST = [Space(int(c.split(",")[0]), c.split(",")[1], c.split(",")[2])
              for c in SPACE_LIST]
