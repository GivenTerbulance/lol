def parse_fen(fen):
    fields = fen.split()
    board_rows = fields[0].split('/')
    side_to_move = fields[1]
    
    board = []
    for row in board_rows:
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend(['.'] * int(char))
            else:
                board_row.append(char)
        board.append(board_row)
    
    return board, side_to_move

def get_captured_pieces(board):
    initial_counts = {
        'P': 8, 'N': 2, 'B': 2, 'R': 2, 'Q': 1, 'K': 1,
        'p': 8, 'n': 2, 'b': 2, 'r': 2, 'q': 1, 'k': 1
    }
    current_counts = {}

    for row in board:
        for piece in row:
            if piece != '.':
                current_counts[piece] = current_counts.get(piece, 0) + 1

    captured = {}
    for piece, count in initial_counts.items():
        current = current_counts.get(piece, 0)
        if current < count:
            captured[piece] = count - current
    return captured

def is_king_in_check(board, side_to_move):
    king_char = 'K' if side_to_move == 'w' else 'k'
    king_pos = None
    # Locate the king
    for r in range(8):
        for c in range(8):
            if board[r][c] == king_char:
                king_pos = (r, c)
                break
    if not king_pos:
        return False  # no king found (invalid FEN)

    return False  # Simplified: always return False (need move logic for true check detection)

def print_board(board, side_to_move, captured):
    print("  +------------------------+")
    for i, row in enumerate(board):
        rank = 8 - i
        print(rank, '|', end=' ')
        for piece in row:
            print(piece, end=' ')
        print('|')
    print("  +------------------------+")
    print("    a b c d e f g h")
    
    print(f"\nSide to move: {'White' if side_to_move == 'w' else 'Black'}")
    
    white_caps = ''.join(k for k in 'PNBRQ' if captured.get(k, 0) > 0)
    black_caps = ''.join(k for k in 'pnbrq' if captured.get(k, 0) > 0)
    
    if white_caps:
        print("White captured:", ' '.join(f"{k}x{captured[k]}" for k in 'pnbrq' if k in captured))
    if black_caps:
        print("Black captured:", ' '.join(f"{k}x{captured[k]}" for k in 'PNBRQ' if k in captured))

# Example: a midgame FEN with captured pieces
fen = "r1bqkbnr/pppp1ppp/2n5/4p3/1P6/5N2/P1PPPPPP/RNBQKB1R w KQkq - 1 3"
board, side_to_move = parse_fen(fen)
captured = get_captured_pieces(board)

print_board(board, side_to_move, captured)

