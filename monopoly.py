# Author: Filippo Pisello
from cell import Space
from player import Player

def game_analytics(interations=100, players=5, turns=100):
    """
    Returns a dict storing info on the number of stops for the various cells of
    the monopoly board

    -------------
    The dict is in the following form, given n iterations:
    {"Position" : int, "Type" : str, "Color" : str, "Stops for iteration 1" : int,
    ..., "Stops for iteration n" : int}
    """
    output_dict = {"Position":[], "Type":[], "Color":[]}
    for iteration in range(interations):
        iteration_label = f"Stops #{iteration + 1}"
        spaces = game(players, turns)
        if iteration == 0:
            for space in spaces:
                output_dict["Position"].append(space.position)
                output_dict["Type"].append(space.type)
                output_dict["Color"].append(space.color)
        output_dict[iteration_label] = [x.stops for x in spaces]
    return output_dict

def game(number_of_players=5, turns=100):
    """
    Main function regulating the complete game process. It simulates the movements
    along the board in a monopoly game.
    """
    TURN = 0
    PLAYERS_LIST = game_players(number_of_players)
    SPACE_LIST = game_spaces()
    for play in range(number_of_players * turns + 1):
        active_player = find_player(TURN, PLAYERS_LIST)
        turn_events(active_player, SPACE_LIST)
        while active_player.double_dice is not None:
            if active_player.double_dice == 3:
                active_player.to_jail()
            else:
                turn_events(active_player, SPACE_LIST)
        TURN = (TURN + 1) % number_of_players
    return SPACE_LIST

def game_players(number_of_players):
    return [Player(number) for number in range(number_of_players)]

def game_spaces():
    space_generator = open("Cells.txt", "r").read()
    space_generator = space_generator.split("||")[1:]
    return [Space(int(c.split(",")[0]), c.split(",")[1], c.split(",")[2])
            for c in space_generator]

def turn_events(player, cell_list):
    """
    Captures the chain of events which modify the board parameters
    """
    # How the player moves
    player.player_turn()

    # Where he/she gets to
    destination_cell = find_cell(player, cell_list)
    # Registering that a player stopped in that cell
    destination_cell.stops = destination_cell.stops + 1

    # Applying to the player the cell effect, if any
    destination_cell.apply_effect(player)

def find_player(turn, players_list):
    """
    Returns the player obj which is active based on the turn
    """
    for player in players_list:
        if player.id == turn:
            return player

def find_cell(player, cell_list):
    """
    Returns the space obj corresponding to the position reached by a player
    """
    for cell in cell_list:
        if cell.position == player.position:
            return cell

game_analytics(100)