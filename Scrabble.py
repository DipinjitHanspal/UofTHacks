import random
import string

# This is a global variable that keeps track of the turn number.
turn_number = 0


class Player:
    """
    A user-controlled player in a scrabble game.
    @type name: str
        This is the name of the player.
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


class Dictionaries:
    """
    The two major dictionaries we'll need for this game.
    @type letters: list
    @type points: list
    @type amounts: list
    @type letters_points: dict[str:int]
    @type letters_amounts: dict[str:int]
    """

    def __init__(self):
        """
        Initializes a new set of dictionaries.
        @type self: dictionaries
        @rtype: None
        """
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
        self.amounts = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
        self.letters_points = self.make_letter_points_dict()
        self.letters_amounts = self.make_letter_amounts_dict()

    def make_letter_points_dict(self):
        """
        Makes a dictionary containing the letters mapped to point values.
        """
        letter_points_dict = {}
        for i in range(len(self.letters)):
            letter_points_dict[self.letters[i]] = self.points[i]
        return letter_points_dict

    def make_letter_amounts_dict(self):
        """
        Makes a dictionary containing the letters mapped to quantity values.
        """
        letter_amounts_dict = {}
        for i in range(len(self.letters)):
            letter_amounts_dict[self.letters[i]] = self.amounts[i]
        return letter_amounts_dict


def generate_tiles(num_tiles, curr_hand=[]):
    """
    Generates a random starting hand for an entity.
    Effectively, this takes your still-existing hand of tiles (by default it's empty), and adds
    tiles from the back of a finite tile list for as many tiles are missing.

    @type num_tiles: int
        This is the number of tiles that needs to be refilled for that entity's hand.
    @type curr_hand: list[Tile]
        This is the leftover tiles from the entity's hand.
    @rtype: list[Tile]
    """
    new_hand = curr_hand
    for i in range(num_tiles):
        # for this to work, we MUST create a Dictionaries object called "dic"...
        rand_letter = random.choice(string.ascii_lowercase)

        # While the random letter chosen has no more available tiles, keep selecting another random letter
        while dic.letters_amounts[rand_letter] == 0:
            rand_letter = random.choice(string.ascii_lowercase)

        # Then, subtract 1 from that letter's amount, and create a new tile with it, which we'll eventually return
        dic.letters_amounts[rand_letter] -= 1
        new_tile = Tile(rand_letter, dic.letters_points[rand_letter])
        new_hand.append(new_tile)

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

if __name__ == '__main__':
    # dic = Dictionaries()
    # print(dic.letters_amounts)
    # print(dic.letters_points)
    # print(random.choice(string.ascii_lowercase))
