"""
The cake is not a lie!
======================

Commander Lambda has had an incredibly successful week: the first test of the LAMBCHOP doomsday device was completed AND
Lambda set a new personal high score in Tetris. To celebrate, the Commander ordered cake for everyone -- even the
lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for
everyone you'll get in big trouble.

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the
M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda
hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each
possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise
(the decorations form a circle around the outer edge of the cake).

Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the
sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.
"""


def solution(s):
    index = [i for i in range(2, len(s)+1) if len(s) % i == 0]

    for i in reversed(index):
        str_size = int(len(s) / i)

        counter = 0
        f_list = []

        str_end = str_size * (counter + 1)

        while str_end < len(s):

            str_start = str_size * counter
            str_end = str_size * (counter + 1)

            f_list.append(s[str_start:str_end])

            counter += 1

        print(f_list)

        if len(set(f_list)) <= 1:
            print(i)
            return i

    return 1



solution("abcabcabcabc")
