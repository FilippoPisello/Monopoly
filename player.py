# Author: Filippo Pisello
import random

class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.position = 0
        self.jail_counter = None
        self.score1 = 0
        self.score2 = 0
        self.double_dice = None

    def player_turn(self):
        """
        Set of actions occuring when it is player's X turn
        """
        self.two_dices_throw()
        self.check_double_dice()
        if not self.check_jail():
            self.update_position()
        return

    def update_position(self):
        self.position = (self.position + self.score1 + self.score2) % 40

    def check_jail(self):
        """
        Returns True if player remains in jail, False if it moves
        """
        if self.position == 10 and self.jail_counter is not None:
            self.jail_counter = self.jail_counter + 1
            if self.double_dice or self.jail_counter == 3:
                self.jail_counter = -1
            else:
                return True
        return False

    def check_double_dice(self):
        """
        Increases by 1 double dices counter if player made double dices.
        """
        if self.score1 == self.score2 and self.jail_counter != -1:
            try:
                self.double_dice = self.double_dice + 1
            except TypeError:
                self.double_dice = 1
        else:
            self.double_dice = None
        return

    def to_jail(self):
        """
        Updates player position and jail counter.
        """
        self.position = 10
        self.jail_counter = 0
        self.double_dice = None
        return

    def two_dices_throw(self):
        self.score1, self.score2 = self.random_int(elements=2, min_value=1, max_value=6)

    @staticmethod
    def random_int(elements, min_value, max_value):
        """
        Returns n integers in range (min_value, max_value + 1), where n is equal
        to elements.
        """
        return [random.randint(min_value, max_value) for x in range(elements)]

PLAYERS_LIST = [Player(number) for number in range(5)]
