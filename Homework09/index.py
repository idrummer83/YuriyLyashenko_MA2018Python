"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
import random
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans


def permutation(outcomes, length):

    ans = set([()])
    for dummy_idx in range(length):
        temp = []
        for seq in ans:
            for item in outcomes:
                if item not in seq or seq.count(item) < outcomes.count(item):
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.append(tuple(new_seq))
        ans = temp
    return ans


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    score_res = [hand.count(i) * i for i in hand]
    return max(score_res)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    all_seq = gen_all_sequences((range(1,(num_die_sides+1))),num_free_dice)
    all_hands = [h + held_dice for h in all_seq]
    number_of_outcomes = float(len(all_seq))
    max_num = 0

    for hand in all_hands:
        max_num += (1/number_of_outcomes)*score(hand)
    return max_num


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = set([()])
    for l in range(len(hand)+1):
        all_permutation = permutation(hand, l)
        all_combinations = [tuple(sorted(sequence)) for sequence in all_permutation]
        all_holds.update(all_combinations)
    return all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = list(gen_all_holds(hand))

    max_val = 0
    val_list = []
    for hold in all_holds:
        expected_value_num = expected_value(hold,num_die_sides,len(hand)-len(hold))
        val_list.append(expected_value_num)
        if expected_value_num > max_val:
            max_val = expected_value_num
    hold_choice = []

    for v in range(len(val_list)):
        if val_list[v] == max_val:
            hold_choice.append(all_holds[v])

    return (max_val, hold_choice)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


run_example()


#from poc_holds_testsuite import run_suite
#run_suite(gen_all_holds)

