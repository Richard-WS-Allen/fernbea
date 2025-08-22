"""Contains UCI handler class."""

import chess


class UciHandler:
    """Class to handle interactions with UCI and parse UCI communications."""
    ID = 'fernbea'
    AUTHOR = 'rwsa'


    def __init__(self):
        self.board = chess.Board()


    def loop(self):
        """Accepts input from a UCI GUI"""
        while True:
            line = input()
            parts = line.split()
            cmd = parts[0]
            if cmd == 'quit' or cmd == 'stop':
                break
            elif cmd == 'uci':
                print('id name fernbea')
                print('author name rwsa')
                print('uciok')
            elif cmd == 'setoption':
                continue
            elif cmd == 'isready':
                print('readyok')
            elif cmd == 'go':
                continue
            elif cmd == 'position':
                continue
            elif cmd == 'eval':
                continue
            elif cmd == 'ucinewgame':
                self.board = chess.Board()
                if len(parts) > 2:
                    if parts[2] == 'moves':
                        for move_str in parts[3:]:
                            self.board.push(chess.Move.from_uci(move_str))
                    else:
                        self.board = chess.Board(" ".join(parts[2:]))
            elif cmd == 'flip':
                continue
            elif cmd == 'ponderhit':
                continue
