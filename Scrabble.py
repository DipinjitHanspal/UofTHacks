import random
import string

# This is a global integer that keeps track of the turn number.
turn_number = 0
# This is a global integer that keeps track of the tiles left.
tiles_left = 100
# This is a global list variable for the current Dictionary object.
curr_dicts = []
# This is a global integer for determining iff both sides cannot make more moves (passed).
game_end = 0


class ScrabbleGame:
    # To start everything, we basically make an instance of ScrabbleGame in __main__() and go from there.
    """
    A game of Scrabble. It'll be fun...I hope.
    @type p1: Player
        The user-player of this game.
    @type p2: AI
        The computer-player of this game.
    @type dic: Dictionaries
        The set of dictionaries and word_list this game will refer to.
    """

    def __init__(self):
        """
        Starting a new game.
        @type self: ScrabbleGame
        @rtype: None
        """
        name = input("Please enter the player's name: ")
        # Firstly initializes the dictionary, as p1 and p2 will need them.
        self.dic = Dictionaries()
        global curr_dicts
        curr_dicts.append(self.dic.letters_points)
        curr_dicts.append(self.dic.letters_amounts)
        curr_dicts.append(self.dic.word_list)

        # Now initializes the Player, the AI, and the method simulating the start of the game.
        self.p1 = Player(name)
        self.p2 = AI()
        self.game()

    def game(self):
        """
        The game's entirety, I think.
        @type self: ScrabbleGame
        @rtype: str
        """
        print("The game begins...")
        global curr_dicts
        global turn_number
        global tiles_left

        # Calls the turn_start method many many times, which facilitates the game's progression.
        # The turns carry on indefinitely until one of the follow conditions is fulfilled:
        # 1) Tiles_left hits 0   2)Both the Player and AI's hands become empty   3) Both player pass in a row
        # 4) It exceeds 200 turns (more to prevent exceptions of infinite loops, as this normally wouldn't happen)
        while tiles_left != 0 and (self.p1.hand != [] and self.p2.hand != []) and game_end <= 1 and turn_number < 200:
            self.turn_start()
            print("It is now turn #" + str(turn_number) + ".")
        curr_dicts = []
        # Returns the winner after the game has technically ended.
        return self.winner()

    def turn_start(self):
        """
        Determines whose turn it is currently, and then allows that entity to make a move.
        It will continue to do this until both sides pass, then it finishes.
        @rtype: None
        """
        global turn_number
        # On even turns (including the first), the Player moves, and on odd turns the AI moves.
        if turn_number % 2 == 0:
            print("Tis " + self.p1.name + "'s turn!")
            self.p1.player_move()
        else:
            print("Tis " + self.p2.name + "'s turn!")
            self.p2.ai_move()

    def winner(self):
        """
        Determines who is the winner at the end of the game, based purely on points.
        @rtype: str
        """
        if self.p1.points > self.p2.points:
            return self.p1.name + "wins!"
        elif self.p2.points > self.p1.points:
            return self.p2.name + "wins!"
        else:
            return "Aw...it's a tie..."


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
        self.hand = self.generate_tiles(7)
        self.points = 0

    def player_move(self):
        """
        When a player decides to play a tile (or word).
        @type self: Player
        @rtype: bool
        """
        global turn_number
        global game_end
        turn_number += 1
        # if ipass:             # This is the unimplimented if block for passing
        #    game_end += 1
        # else:
        point_gain = 0  # We'll need to change this to the actual point gain later
        self.update_points(point_gain)
        # This refills the Player's hand
        self.hand = self.generate_tiles(7 - len(self.hand), self.hand)
        game_end = 0

    def generate_tiles(self, num_tiles, curr_hand=[]):
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
        # If there aren't enough tiles to fill that person's hand, then give them as many as are leftover in the pile.
        global tiles_left
        if num_tiles > tiles_left:
            num_tiles = tiles_left

        for i in range(num_tiles):
            # We're looping through and creating a tile object with the help of our dictionaries
            rand_letter = random.choice(string.ascii_lowercase)

            # While the random letter chosen has no more available tiles, keep selecting another random letter
            global curr_dicts
            while curr_dicts[1][rand_letter] == 0:
                rand_letter = random.choice(string.ascii_lowercase)

            # Then, subtract 1 from that letter's amount, and create a new tile with it, which we'll eventually return
            curr_dicts[1][rand_letter] -= 1
            new_tile = Tile(rand_letter, curr_dicts[0][rand_letter])
            new_hand.append(new_tile)
            tiles_left -= 1

        return new_hand

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
        self.hand = self.generate_tiles(7)
        self.points = 0

    def ai_move(self):
        """
        When the AI decides to play a tile (or word).
        @type self: AI
        @rtype: bool
        """
        global turn_number
        global game_end
        turn_number += 1
        # if youpass:             # This is the unimplimented if block for passing
        #    game_end += 1
        # else:
        point_gain = 0  # We'll need to change this to the actual point gain later
        self.update_points(point_gain)
        # This refills the AI's hand
        self.hand = self.generate_tiles(7 - len(self.hand), self.hand)
        game_end = 0

    def generate_tiles(self, num_tiles, curr_hand=[]):
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

        global tiles_left
        if num_tiles > tiles_left:
            num_tiles = tiles_left

        for i in range(num_tiles):
            rand_letter = random.choice(string.ascii_lowercase)

            global curr_dicts
            while curr_dicts[1][rand_letter] == 0:
                rand_letter = random.choice(string.ascii_lowercase)

            curr_dicts[1][rand_letter] -= 1
            new_tile = Tile(rand_letter, curr_dicts[0][rand_letter])
            new_hand.append(new_tile)
            tiles_left -= 1

        return new_hand

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
    A combined object comprising of two major dictionaries and one big list we'll need for this game, specifically
    letter:points, letter:quantity, and word_list.
    @type letters: list
        A list that contains all the possible letters.
    @type points: list
        A list that contains all the possible points.
    @type amounts: list
        A list that contains all the possible quantities.
    @type letters_points: dict[str:int]
        A dictionary that contains all the points corresponding to the letters.
    @type letters_amounts: dict[str:int]
        A dictionary that contains all the quantities corresponding to the letters.
    @type word_list: list[str]
        A list that contains all the words available to use.
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
        self.word_list = self.make_word_list()

    def make_letter_points_dict(self):
        """
        Makes a dictionary containing the letters mapped to point values.
        @type self: dictionaries
        @rtype: dict[str:int]
        """
        letter_points_dict = {}
        for i in range(len(self.letters)):
            letter_points_dict[self.letters[i]] = self.points[i]
        return letter_points_dict

    def make_letter_amounts_dict(self):
        """
        Makes a dictionary containing the letters mapped to quantity values.
        @type self: dictionaries
        @rtype: dict[str:int]
        """
        letter_amounts_dict = {}
        for i in range(len(self.letters)):
            letter_amounts_dict[self.letters[i]] = self.amounts[i]
        return letter_amounts_dict

    def make_word_list(self):
        """
        Makes the big list of words that can be played in the game.
        @type self: Dictionaries
        @rtype: list[str]
        """
        word_list = []

        f_open = open("dictionary.csv", "r")
        for line in f_open:
            word_list.append(line.strip("\n").strip("\r"))
        f_open.close()

        return word_list


def is_modified(points, modifier):
    """
    Determines the modification (multiplying) of a tile's value. (Currently does nothing!)
    @type points: int
    @type modifier: int
    @rtype: int
    """
    return points*modifier


if __name__ == '__main__':
    newgame = ScrabbleGame()
