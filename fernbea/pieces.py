"""Includes classes for chess pieces and board."""

from textwrap import wrap


WHITE = False
BLACK = True
PW_START_POS = int( \
    "11111111" \
    "00000000", 2)
PB_START_POS = PW_START_POS << 40
NW_START_POS = int( \
    "01000010", 2)
NB_START_POS = NW_START_POS << 56
BW_START_POS = int( \
    "00100100", 2)
BB_START_POS = BW_START_POS << 56
RW_START_POS = int( \
    "10000001", 2)
RB_START_POS = RW_START_POS << 56
QW_START_POS = int( \
    "00010000", 2)
QB_START_POS = QW_START_POS << 56
KW_START_POS = int( \
    "00001000", 2)
KB_START_POS = KW_START_POS << 56

PAWN = 0
KNIGHT = 1
BISHOP = 2
ROOK = 3
QUEEN = 4
KING = 5

# Unicode chess pieces
PIECE_TABLE = [
    ['\u265F',  # white pawn
     '\u265E',  # white knight
     '\u265D',  # white bishop
     '\u265C',  # white rook
     '\u265B',  # white queen
     '\u265A',  # white king
     ],
    ['\u2659',  # black pawn
     '\u2658',  # black knight
     '\u2657',  # black bishop
     '\u2656',  # black rook
     '\u2655',  # black queen
     '\u2654',  # black king
     ]
]


def bb_to_piece_index(bb: int = 0):
    """Converts the bitboard into piece positions as an index of a len(64) array"""
    indices = []
    i = 0
    while bb > 0:
        if bb % 2 == 1:
            indices.append(i)
        bb = bb >> 1
        i += 1
    return indices


class Piece:
    """Super class for chess pieces.
    'color': Notes piece color. Should either be 0 (WHITE) or 1 (BLACK)
    'bb': The pieces bitboard representation.
    'uni_rep': The unicode character to represent the piece in CLI."""
    color = WHITE
    bb = 0
    uni_rep = ''
    def __init__(
            self,
            color: int = 0,
            bb: int = 0,
            uni_rep: str = ''
        ):
        self.color = color
        self.bb = bb
        self.uni_rep = uni_rep


    def __str__(self):
        return self.uni_rep


class Pawn(Piece):
    """
    Subclass of Piece.
    'bb': Bitboard for the set of pawns. If None, starting position is used"""
    def __init__(self, color: int, bb: int | None):
        if bb is None:
            if color:
                bb = PB_START_POS
            else:
                bb = PW_START_POS
        super().__init__(
            color=color,
            bb=bb,
            uni_rep=PIECE_TABLE[color][PAWN]
        )


class Knight(Piece):
    """
    Subclass of Piece.
    'bb': Bitboard for the set of knights. If None, starting position is used"""
    def __init__(self, color: int, bb: int | None):
        if bb is None:
            if color:
                bb = NB_START_POS
            else:
                bb = NW_START_POS
        super().__init__(
            color=color,
            bb=bb,
            uni_rep=PIECE_TABLE[color][KNIGHT]
        )


class Bishop(Piece):
    """
    Subclass of Piece.
    'bb': Bitboard for the set of bishops. If None, starting position is used"""
    def __init__(self, color: int, bb: int | None):
        if bb is None:
            if color:
                bb = BB_START_POS
            else:
                bb = BW_START_POS
        super().__init__(
            color=color,
            bb=bb,
            uni_rep=PIECE_TABLE[color][BISHOP]
        )


class Rook(Piece):
    """
    Subclass of Piece.
    'bb': Bitboard for the set of rooks. If None, starting position is used"""
    def __init__(self, color: int, bb: int | None):
        if bb is None:
            if color:
                bb = RB_START_POS
            else:
                bb = RW_START_POS
        super().__init__(
            color=color,
            bb=bb,
            uni_rep=PIECE_TABLE[color][ROOK]
        )


class Queen(Piece):
    """
    Subclass of Piece.
    'bb': Bitboard for a queen. If None, starting position is used"""
    def __init__(self, color: int, bb: int | None):
        if bb is None:
            if color:
                bb = QB_START_POS
            else:
                bb = QW_START_POS
        super().__init__(
            color=color,
            bb=bb,
            uni_rep=PIECE_TABLE[color][QUEEN]
        )


class King(Piece):
    """
    Subclass of Piece.
    'bb': Bitboard for the king. If None, starting position is used"""
    def __init__(self, color: int, bb: int | None):
        if bb is None:
            if color:
                bb = KB_START_POS
            else:
                bb = KW_START_POS
        super().__init__(
            color=color,
            bb=bb,
            uni_rep=PIECE_TABLE[color][KING]
        )


class Board:
    """
    Contains the bitboards for a game of chess."""
    bb_idx_to_str_idx_table = list(reversed(range(64)))
    board = [[
                Pawn(color=WHITE, bb=None),
                Knight(color=WHITE, bb=None),
                Bishop(color=WHITE, bb=None),
                Rook(color=WHITE, bb=None),
                Queen(color=WHITE, bb=None),
                King(color=WHITE, bb=None),
            ], [
                Pawn(color=BLACK, bb=None),
                Knight(color=BLACK, bb=None),
                Bishop(color=BLACK, bb=None),
                Rook(color=BLACK, bb=None),
                Queen(color=BLACK, bb=None),
                King(color=BLACK, bb=None),
            ],
        ]


    def __iter__(self):
        for color in self.board:
            for piece in color:
                yield piece


    def __str__(self):
        # Using '.' as empty squares.
        board_list = ['.' for _ in range(64)]

        for piece in self:
            indices = bb_to_piece_index(piece.bb)
            for i in indices:
                board_list[self.bb_idx_to_str_idx_table[i]] = str(piece)
        return '\n'.join(wrap(''.join(board_list), 8))
