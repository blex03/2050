def solveable(p_idxs, k_idx):
    if not p_idxs:
        return True

    moves = valid_moves(k_idx)

    count = 0
    for i in moves:
        if i in p_idxs:
            count += 1

            p_idxs.remove(i)
            if solveable(p_idxs, i) == True:
                return True

    return False


def valid_moves(k_idx):
    moves = set()
    moves.add((k_idx[0] - 1, k_idx[1] - 2))
    moves.add((k_idx[0] - 1, k_idx[1] + 2))
    moves.add((k_idx[0] - 2, k_idx[1] - 1))
    moves.add((k_idx[0] - 2, k_idx[1] + 1))
    moves.add((k_idx[0] + 1, k_idx[1] - 2))
    moves.add((k_idx[0] + 1, k_idx[1] + 2))
    moves.add((k_idx[0] + 2, k_idx[1] - 1))
    moves.add((k_idx[0] + 2, k_idx[1] + 1))

    final_moves = set()

    for i in moves:
        if i[0] >= 0 and i[0] <= 7 and i[1] >= 0 and i[1] <= 7:
            final_moves.add(i)

    return final_moves


