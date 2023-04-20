from app.models import Move


def create_moves_json(moves):
    moves_tmp = list(moves)
    username_1 = moves_tmp[0].user.username
    username_2 = ''
    username_1_moves = []
    username_2_moves = []
    prev_checker_moves = [['a1'], ['c1'], ['e1'], ['g1'],
                          ['b2'], ['d2'], ['f2'], ['h2'],
                          ['a3'], ['c3'], ['e3'], ['g3'],
                          ['h8'], ['f8'], ['d8'], ['b8'],
                          ['g7'], ['e7'], ['c7'], ['a7'],
                          ['h6'], ['f6'], ['d6'], ['b6']]

    for move in moves_tmp:
        if move.user.username != username_1 and username_2 == '':
            username_2 = move.user.username
        if (len(move.new_positions) == 1 and prev_checker_moves[move.checker_id][0] != move.new_positions[0] or len(move.new_positions) > 1):
            if move.user.username == username_1:
                username_1_moves.append(
                    prev_checker_moves[move.checker_id] + move.new_positions)
            else:
                username_2_moves.append(
                    prev_checker_moves[move.checker_id] + move.new_positions)
        prev_checker_moves[move.checker_id] = move.new_positions[::-1]
    return {username_1: username_1_moves, username_2: username_2_moves}


def create_start_moves(game, usr_1, usr_2):
    return [
        Move(game=game, user=usr_1, checker_id=0, new_positions=['a1']),
        Move(game=game, user=usr_1, checker_id=1, new_positions=['c1']),
        Move(game=game, user=usr_1, checker_id=2, new_positions=['e1']),
        Move(game=game, user=usr_1, checker_id=3, new_positions=['g1']),
        Move(game=game, user=usr_1, checker_id=4, new_positions=['b2']),
        Move(game=game, user=usr_1, checker_id=5, new_positions=['d2']),
        Move(game=game, user=usr_1, checker_id=6, new_positions=['f2']),
        Move(game=game, user=usr_1, checker_id=7, new_positions=['h2']),
        Move(game=game, user=usr_1, checker_id=8, new_positions=['a3']),
        Move(game=game, user=usr_1, checker_id=9, new_positions=['c3']),
        Move(game=game, user=usr_1, checker_id=10, new_positions=['e3']),
        Move(game=game, user=usr_1, checker_id=11, new_positions=['g3']),
        Move(game=game, user=usr_2, checker_id=12,
             new_positions=['h8'], is_white=False),
        Move(game=game, user=usr_2, checker_id=13,
             new_positions=['f8'], is_white=False),
        Move(game=game, user=usr_2, checker_id=14,
             new_positions=['d8'], is_white=False),
        Move(game=game, user=usr_2, checker_id=15,
             new_positions=['b8'], is_white=False),
        Move(game=game, user=usr_2, checker_id=16,
             new_positions=['g7'], is_white=False),
        Move(game=game, user=usr_2, checker_id=17,
             new_positions=['e7'], is_white=False),
        Move(game=game, user=usr_2, checker_id=18,
             new_positions=['c7'], is_white=False),
        Move(game=game, user=usr_2, checker_id=19,
             new_positions=['a7'], is_white=False),
        Move(game=game, user=usr_2, checker_id=20,
             new_positions=['h6'], is_white=False),
        Move(game=game, user=usr_2, checker_id=21,
             new_positions=['f6'], is_white=False),
        Move(game=game, user=usr_2, checker_id=22,
             new_positions=['d6'], is_white=False),
        Move(game=game, user=usr_2, checker_id=23,
             new_positions=['b6'], is_white=False),
    ]
