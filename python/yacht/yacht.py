# Score categories.
# Change the values as you see fit.
from collections import Counter


YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    if category == CHOICE:
        return sum(dice)

    if category == BIG_STRAIGHT:
        return 30 if set(dice) == set(range(2, 7)) else 0

    if category == LITTLE_STRAIGHT:
        return 30 if set(dice) == set(range(1, 6)) else 0

    if category == FOUR_OF_A_KIND:
        counts = Counter(dice)
        common_value = counts.most_common(1)[0]
        if common_value[1] >= 4:
            return common_value[0] * 4

    if category == FULL_HOUSE:
        counts = Counter(dice)
        common_values = counts.most_common(2)
        if common_values[0][1] == 3 and common_values[1][1] == 2:
            return common_values[0][0] * 3 + common_values[1][0] * 2

    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return sum(value for value in dice if value == category)

    return 0
