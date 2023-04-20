from app.models import Move


def create_moves_json(moves):
    moves_tmp = list(moves)
    username_1 = moves_tmp[0].user.username
    username_2 = ''
    username_1_moves = []
    username_2_moves = []
    tmp_moves_array = []
    prev_username = username_1
    prev_checker_position = [['a1', 'h8'], ['c1', 'f8'], ['e1', 'd8'], ['g1', 'b8'],
                             ['b2', 'g7'], ['d2', 'e7'], [
                                 'f2', 'c7'], ['h2', 'a7'],
                             ['a3', 'h6'], ['c3', 'f6'], ['e3', 'd6'], ['f3', 'b6']]
    for move in moves_tmp:
        if move.user.username == username_1:
            if prev_username != username_1:
                username_2_moves.append(tmp_moves_array)
                tmp_moves_array = []
                prev_username = move.user.username
        else:
            if username_2 == '':
                username_2 = move.user.username
            if prev_username == username_1:
                username_1_moves.append(tmp_moves_array)
                tmp_moves_array = []
                prev_username = move.user.username
        tmp_moves_array.append(prev_checker_position[move.checker_id][int(
            not move.is_white)] + '-' + move.new_position)
        prev_checker_position[move.checker_id][int(
            not move.is_white)] = move.new_position
    if prev_username == username_1:
        username_1_moves.append(tmp_moves_array)
    else:
        username_2_moves.append(tmp_moves_array)
    return {username_1: username_1_moves, username_2: username_2_moves}


def create_start_moves(game, usr_1, usr_2):
    return [
        Move(game=game, user=usr_1, checker_id=0, new_position='a1'),
        Move(game=game, user=usr_1, checker_id=1, new_position='c1'),
        Move(game=game, user=usr_1, checker_id=2, new_position='e1'),
        Move(game=game, user=usr_1, checker_id=3, new_position='g1'),
        Move(game=game, user=usr_1, checker_id=4, new_position='b2'),
        Move(game=game, user=usr_1, checker_id=5, new_position='d2'),
        Move(game=game, user=usr_1, checker_id=6, new_position='f2'),
        Move(game=game, user=usr_1, checker_id=7, new_position='h2'),
        Move(game=game, user=usr_1, checker_id=8, new_position='a3'),
        Move(game=game, user=usr_1, checker_id=9, new_position='c3'),
        Move(game=game, user=usr_1, checker_id=10, new_position='e3'),
        Move(game=game, user=usr_1, checker_id=11, new_position='g3'),
        Move(game=game, user=usr_2, checker_id=12,
             new_position='h8', is_white=False),
        Move(game=game, user=usr_2, checker_id=13,
             new_position='f8', is_white=False),
        Move(game=game, user=usr_2, checker_id=14,
             new_position='d8', is_white=False),
        Move(game=game, user=usr_2, checker_id=15,
             new_position='b8', is_white=False),
        Move(game=game, user=usr_2, checker_id=16,
             new_position='g7', is_white=False),
        Move(game=game, user=usr_2, checker_id=17,
             new_position='e7', is_white=False),
        Move(game=game, user=usr_2, checker_id=18,
             new_position='c7', is_white=False),
        Move(game=game, user=usr_2, checker_id=19,
             new_position='a7', is_white=False),
        Move(game=game, user=usr_2, checker_id=20,
             new_position='h6', is_white=False),
        Move(game=game, user=usr_2, checker_id=21,
             new_position='f6', is_white=False),
        Move(game=game, user=usr_2, checker_id=22,
             new_position='d6', is_white=False),
        Move(game=game, user=usr_2, checker_id=23,
             new_position='b6', is_white=False),
    ]
