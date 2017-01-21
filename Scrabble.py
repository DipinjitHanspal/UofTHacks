import random

# This is a global variable that keeps track of the turn number.
turn_number = 0


class Player:
    """
    A user-controlled player in a scrabble game.
    @type name: str
        This is the name of the player.
    @type isturn: bool
        If it is the player's turn or not.
    @type hand: list[Tile]
        The player's hand of tiles, each tile is a tile object.
    @type points: int
        How many points the player has accumulated.
    """

    def __init__(self, username):
        """
        Initializes a new player in a scrabble game.
        @type self: Player
        @type username: str
        @rtype: None
        """
        # This may be changed to a python input though
        self.name = username
        self.isturn = True
        self.hand = generate_tiles(7)
        self.points = 0

    def player_move(self):
        """
        When a player decides to play a tile (or word).
        @type self: Player
        @rtype: None
        """
        global turn_number
        turn_number += 1
        self.hand = generate_tiles(7 - len(self.hand), self.hand)

    def update_points(self, points):
        """
        Adds points to an Player, at the end of their turn.
        @type self: Player
        @type points: int
        @rtype: None
        """
        self.points += points


class AI:
    """
    A computer-controlled opponent in a scrabble game.
    @type name: str
        This is the name of the AI, it's always the same (at least for now).
    @type isturn: bool
        If it is the AI's turn or not.
    @type hand: list[Tile]
        The AI's hand of tiles, each tile is a tile object.
    @type points: int
        How many points the AI has accumulated.
    """

    def __init__(self):
        """
        Initializes a new AI in a scrabble game.
        @type self: AI
        @rtype: None
        """
        self.name = "Your Worst Nightmare MUAHAHA"
        self.isturn = False
        self.hand = generate_tiles(7)
        self.points = 0

    def ai_move(self):
        """
        When the AI decides to play a tile (or word).
        @type self: AI
        @rtype: None
        """
        global turn_number
        turn_number += 1
        self.hand = generate_tiles(7 - len(self.hand), self.hand)

    def update_points(self, points):
        """
        Adds points to the AI, at the end of their turn.
        @type self: AI
        @type points: int
        @rtype: None
        """
        self.points += points


class Tile:
    """
    A tile in a scrabble game.
    @type letter: str
        The letter that is on the tile.
    @type value: int
        The amount of points the tile is worth.
    """

    def __init__(self, letter, points):
        """
        Initializes a new AI in a scrabble game.
        @type self: Tile
        @rtype: None
        """
        self.letter = letter
        self.value = points


def generate_tiles(num_tiles, curr_hand=[]):
    """
    Generates a random starting hand for an entity.
    @type num_tiles: int
        This is the number of tiles that needs to be refilled for that entity's hand.
    @type curr_hand: list[Tile]
        This is the leftover tiles from the entity's hand.
    @rtype: list[tile]
    """
    new_hand = curr_hand
    for i in range(num_tiles):
        # if we're having a pre-generate finite set of tiles
        new_hand.append([finite_tile_list].pop())
    return new_hand


def is_modified(points, modifier):
    """
    Determines the modification (multiplying) of a tile's value.
    @type points: int
    @type modifier: int
    @rtype: int
    """
    return points*modifier


def turn_start(player, ai):
    """
    Determines whose turn it is currently, and then allows that entity to make a move.
    @type player: Player
    @type ai: AI
    @rtype: None
    """
    global turn_number
    if turn_number % 2 == 0:
        player.player_move()
    else:
        ai.ai_move()


def winner(player, ai):
    """
    Determines who is the winner at the end of the game.
    @type player: Player
    @type ai: AI
    @rtype: str
    """
    if player.points > ai.points:
        return player.name
    else:
        return ai.name
