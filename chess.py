def parse_fen(fen):
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ")
    pieces = [[]]
    for char in fen_pieces:
        if char.isdigit():
            pieces[-1].extend(["."] * int(char))
        elif char == "/":
            pieces.append([])
        else:
            pieces[-1].append(char)

    return pieces

our_pieces = {
    "r": "R", "n": "N", "b": "B", "q": "Q", "k": "K", "p": "P",
    "R": "r", "N": "n", "B": "b", "Q": "q", "K": "k", "P": "p",
    ".": "·"
}

board["p"] = "." 
board["e4"] = "P" 

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board = parse_fen(fen)

row_number = 8 

for row in board:
    print(row_number, end="") 

    for piece in row:
        symbol = our_pieces[piece]  
        print(symbol + "  ", end="")  

    print(row_number)  
    row_number -= 1

def generate_moves(board):
    raise NotImplementedError("This function is not implemented yet.")


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")
print(parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))
