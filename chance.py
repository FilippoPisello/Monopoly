class Chance:
    """
    Class which captures chance cards and relative effects
    """
    def __init__(self, id_):
        self.id = id_

    def apply_effect(self, player):
        """
        Applies the cards effect to the player
        """
        if self.id in range(13):
            pass # no action for the first 13 cards
        if self.id == 13:
            player.position = 1
        if self.id == 14:
            player.position = 0
        if self.id == 15:
            player.to_jail()

CHANCE_LIST = [Chance(x) for x in range(16)]

class CommunityChest:
    """
    Class which captures community chest cards and relative effects
    """
    def __init__(self, id_):
        self.id = id_

    def apply_effect(self, player):
        """
        Applies the card effect to the player
        """
        if self.id in range(9):
            pass # no action for the first 9 cards
        elif self.id == 9:
            player.position = 0
        elif self.id == 10:
            player.position = 25
        elif self.id == 11:
            player.position = 39
        elif self.id == 12:
            player.position = 24
        elif self.id == 13:
            player.position = 11
        elif self.id == 14:
            player.position = player.position - 3
        elif self.id == 15:
            player.to_jail()

COMMUNITY_CHEST_LIST = [CommunityChest(x) for x in range (16)]
