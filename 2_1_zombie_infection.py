# Copyright (c) 2012-2014 Kapiche Limited
# Author: Ryan Stuart <ryan@kapiche.com>
"""
Peculiar balance
================

Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an
obstacle. The  door will only open if a challenge is solved correctly. The future of the zombified rabbit population is
at stake, so Beta reads the  challenge: There is a scale with an object on the left-hand side, whose mass is given in
some number of units. Predictably, the task is to  balance the two sides. But there is a catch: You only have this
peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one  for each power of 3. Being a brilliant
mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced  exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the
weights should be  placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.

The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight,
and so on. Each  string is one of:

"L" : put weight on left-hand side
"R" : put weight on right-hand side
"-" : do not use weight

To ensure that the output is the smallest possible, the last element of the list must not be "-".

x will always be a positive integer, no larger than 1000000000.
"""


def answer(population, x, y, strength):
    constrain_x = len(population[0])
    constrain_y = len(population)
    places_to_vist = [(x, y,)]
    places_visited = []

    def where_next():
        for item in places_to_vist:
            yield item

    for x, y in where_next():
        if population[y][x] <= strength:
            # print "Position ({}, {}) infected... ({} >= {})".format(x, y, population[y][x], strength)
            places_visited.append((x, y,))
            population[y][x] = -1
            if x - 1 >= 0 and (x-1, y,) not in places_visited:
                # print "Adding ({}, {}) to places to visit".format(x-1, y)
                places_to_vist.append((x-1, y,))
            if x + 1 < constrain_x and (x+1, y,) not in places_visited:
                # print "Adding ({}, {}) to places to visit".format(x+1, y)
                places_to_vist.append((x+1, y,))
            if y - 1 >= 0 and (x, y-1,) not in places_visited:
                # print "Adding ({}, {}) to places to visit".format(x, y-1)
                places_to_vist.append((x, y-1,))
            if y + 1 < constrain_y and (x, y+1,) not in places_visited:
                # print "Adding ({}, {}) to places to visit".format(x, y+1)
                places_to_vist.append((x, y+1,))
        # else:
            # print "Position ({}, {}) NOT infected... ({} < {})".format(x, y, population[y][x], strength)
    return population


if __name__ == '__main__':
    print answer([[1, 2, 3], [2, 3, 4], [3, 2, 1]], 0, 0, 2)
    print answer([[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]], 2, 1, 5)
