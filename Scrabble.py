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
        self.hand = gen_start_hand(True)
        self.points = 0

    def player_move(self):
        """
        When a player decides to play a tile (or word).
        @type self: Player
        @rtype: None
        """
        pass


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
        @type self: Player
        @rtype: None
        """
        self.name = "Your Worst Nightmare MUAHAHA"
        self.isturn = False
        self.hand = gen_start_hand(False)
        self.points = 0

    def ai_move(self):
        """
        When the AI decides to play a tile (or word).
        @type self: AI
        @rtype: None
        """
        pass


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



def gen_start_hand(isPlayer):
    """
    Generates a random starting hand for an entity.
    @type isPlayer: bool
    @rtype: list[tile]
    """
    if isPlayer:
        return []
    else:
        return []
