def create_moves_json(moves, user_1, user_2):
    moves_tmp = list(moves)
    username_1 = moves_tmp[0].user.username
    username_2 = user_1 if username_1 == user_2 else user_2
    username_1_moves = []
    username_2_moves = []
    prev_checker_moves = [['a1'], ['c1'], ['e1'], ['g1'],
                          ['b2'], ['d2'], ['f2'], ['h2'],
                          ['a3'], ['c3'], ['e3'], ['g3'],
                          ['h8'], ['f8'], ['d8'], ['b8'],
                          ['g7'], ['e7'], ['c7'], ['a7'],
                          ['h6'], ['f6'], ['d6'], ['b6']]

    for move in moves_tmp:
        if move.user.username == username_1:
            username_1_moves.append(
                prev_checker_moves[move.checkerId] + move.newPositions)
        else:
            username_2_moves.append(
                prev_checker_moves[move.checkerId] + move.newPositions)
        prev_checker_moves[move.checkerId] = move.newPositions[::-1]
    if (not username_1_moves):
        username_1_moves = [[]]
    if (not username_2_moves):
        username_2_moves = [[]]
    return {username_1: username_1_moves, username_2: username_2_moves}
