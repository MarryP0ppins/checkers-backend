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
