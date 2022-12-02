def score_for_outcome(play: []) -> int:
    opponent_possible_moves = ['A', 'B', 'C']
    my_possible_moves = ['X', 'Y', 'Z']

    opponent_move_idx = opponent_possible_moves.index(play[0])
    my_move_idx = my_possible_moves.index(play[1])

    if opponent_move_idx == my_move_idx:
        return 3
    elif (my_move_idx - opponent_move_idx) % 3 == 1:
        return 6
    else:
        return 0


def determine_my_play(code: []) -> []:
    play: [] = code.copy()

    opponent_possible_moves = ['A', 'B', 'C']
    my_possible_moves = ['X', 'Y', 'Z']

    opponent_move_idx = opponent_possible_moves.index(play[0])

    if code[1] == 'Y':
        play[1] = my_possible_moves[opponent_move_idx]
    elif code[1] == 'X':
        play[1] = my_possible_moves[(opponent_move_idx + 2) % 3]
    else:
        play[1] = my_possible_moves[(opponent_move_idx + 1) % 3]

    return play


def score_for_my_move(play: []) -> int:
    my_moves = ['X', 'Y', 'Z']
    return my_moves.index(play[1]) + 1


def calculate_score(play: []) -> int:
    return score_for_my_move(play) + score_for_outcome(play)


def read_input(input_file_name: str) -> []:
    moves = []
    with open(input_file_name) as input_file:
        for line in input_file:
            line = line.strip().split(' ')
            moves.append(line)

    return moves


def main():
    moves = read_input("input.txt")
    print(f"sum of scores pt1: {sum(calculate_score(move) for move in moves)}")
    print(f"sum of scores pt2: {sum(calculate_score(move) for move in [determine_my_play(playbook) for playbook in moves])}")


if __name__ == '__main__':
    main()
