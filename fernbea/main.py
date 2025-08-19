#!/usr/bin/env python3

import chess
import chess.engine

NULL_MOVE = '0000'
ENGINE_ID = 'fernbea'
AUTHOR = 'rwsa'

class FernBeaEngine:
    def __init__(self):
        self.board = chess.Board()

    def uci_loop(self):
        while True:
            # Required to always allow input.
            line = input()
            parts = line.split()

            # TODO: standardize formatting input and responses
            # in a UCI class.
            # TODO: Handle all inputs.
            if parts[0] == "uci":
                print("id name fernbea")
                print("id author rwsa")
                print("uciok")
            elif parts[0] == "isready":
                print("readyok")
            elif parts[0] == "ucinewgame":
                self.board = chess.Board()
            elif parts[0] == "position":
                if parts[1] == "startpos":
                    self.board = chess.Board()
                else: # FEN string
                    self.board = chess.Board(" ".join(parts[2:]))

                if "moves" in parts:
                    move_index = parts.index("moves") + 1
                    for move_uci in parts[move_index:]:
                        move = chess.Move.from_uci(move_uci)
                        self.board.push(move)

            elif parts[0] == "go":
                # Do nothing move for now
                print('0000')

            elif parts[0] == "quit":
                break

if __name__ == "__main__":
    engine = FernBeaEngine()
    engine.uci_loop()
