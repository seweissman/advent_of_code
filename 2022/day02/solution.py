"""
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?


"""


def read_input(file_name):
    """Read lines of input from file"""
    with open(file_name) as file_in:
        lines = [line.strip() for line in file_in.readlines()]
    return lines


from enum import Enum


class RPS(int, Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class State(Enum):
    WIN = 1
    LOSE = 2
    TIE = 3


RPS_MAP_PART1 = {"A": RPS.ROCK, "B": RPS.PAPER, "C": RPS.SCISSORS, "X": RPS.ROCK, "Y": RPS.PAPER, "Z": RPS.SCISSORS}


def game_outcome_part1(opp_play: RPS, your_play: RPS) -> State:
    if your_play == opp_play:
        return State.TIE
    if your_play == RPS.ROCK and opp_play == RPS.PAPER:
        return State.LOSE
    if your_play == RPS.PAPER and opp_play == RPS.SCISSORS:
        return State.LOSE
    if your_play == RPS.SCISSORS and opp_play == RPS.ROCK:
        return State.LOSE
    return State.WIN


def calculate_score_part1(opp_sym: str, your_sym: str) -> int:
    opp_play = RPS_MAP_PART1[opp_sym]
    your_play = RPS_MAP_PART1[your_sym]
    game_state = game_outcome_part1(opp_play, your_play)
    if game_state == State.WIN:
        return 6 + int(your_play)
    if game_state == State.LOSE:
        return int(your_play)
    if game_state == State.TIE:
        return 3 + int(your_play)
    return 0


def test_calculate_score_part1():
    assert calculate_score_part1("A", "X") == 4
    assert calculate_score_part1("A", "Y") == 8
    assert calculate_score_part1("A", "Z") == 3
    assert calculate_score_part1("B", "X") == 1
    assert calculate_score_part1("B", "Y") == 5


RPS_MAP_PART2 = {"A": RPS.ROCK, "B": RPS.PAPER, "C": RPS.SCISSORS, "X": State.LOSE, "Y": State.TIE, "Z": State.WIN}


def calculate_your_play(opp_play: RPS, game_state: State):
    if game_state == State.TIE:
        return opp_play
    if opp_play == RPS.ROCK:
        if game_state == State.WIN:
            return RPS.PAPER
        else:
            return RPS.SCISSORS
    if opp_play == RPS.PAPER:
        if game_state == State.WIN:
            return RPS.SCISSORS
        else:
            return RPS.ROCK
    if opp_play == RPS.SCISSORS:
        if game_state == State.WIN:
            return RPS.ROCK
        else:
            return RPS.PAPER
    return opp_play


def calculate_score_part2(opp_sym: str, your_sym: str) -> int:
    opp_play = RPS_MAP_PART2[opp_sym]
    game_state = RPS_MAP_PART2[your_sym]
    your_play = calculate_your_play(opp_play, game_state)
    if game_state == State.WIN:
        return 6 + int(your_play)
    if game_state == State.LOSE:
        return int(your_play)
    if game_state == State.TIE:
        return 3 + int(your_play)
    return 0


def test_calculate_score_part2():
    assert calculate_score_part2("A", "Y") == 4
    assert calculate_score_part2("B", "X") == 1
    assert calculate_score_part2("C", "Z") == 7


if __name__ == "__main__":
    lines = read_input("input.txt")
    # Part 1
    score = 0
    for line in lines:
        opp_sym, your_sym = line.split()
        round_score = calculate_score_part1(opp_sym, your_sym)
        # print(opp_sym, your_sym, round_score)
        score += round_score

    print(score)

    # part 2

    # Part 1
    score = 0
    for line in lines:
        opp_sym, your_sym = line.split()
        round_score = calculate_score_part2(opp_sym, your_sym)
        # print(opp_sym, your_sym, round_score)
        score += round_score

    print(score)
