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

    def new_tiles(self, needed):
        """
        After the player moves, this method replenishes their hand to have maximum tiles again.
        @type self: Player
        @type needed: int
            This is the number of tiles that will be replenished (how many the player is missing).
        @rtype: list[Tile]
        """
        tiles_returned = []
        for i in range(needed):
            # Do something that generates a Tile called new_tile
            tiles_returned.append(new_tile)
        return tiles_returned

    def player_move(self):
        """
        When a player decides to play a tile (or word).
        @type self: Player
        @rtype: None
        """
        pass

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
        @type self: Player
        @rtype: None
        """
        self.name = "Your Worst Nightmare MUAHAHA"
        self.isturn = False
        self.hand = gen_start_hand(False)
        self.points = 0

    def new_tiles(self, needed):
        """
        After the AI moves, this method replenishes their hand to have maximum tiles again.
        @type self: AI
        @type needed: int
            This is the number of tiles that will be replenished (how many the AI is missing).
        @rtype: list[Tile]
        """
        tiles_returned = []
        for i in range(needed):
            # Do something that generates a Tile called new_tile
            tiles_returned.append(new_tile)
        return tiles_returned

    def ai_move(self):
        """
        When the AI decides to play a tile (or word).
        @type self: AI
        @rtype: None
        """
        pass

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


def gen_start_hand(isplayer):
    """
    Generates a random starting hand for an entity.
    @type isplayer: bool
    @rtype: list[tile]
    """
    if isplayer:
        return []
    else:
        return []


def is_modified(points, modifier):
    """
    Determines the modification (multiplying) of a tile's value.
    @type points: int
    @type modifier: int
    @rtype: int
    """
    return points*modifier
