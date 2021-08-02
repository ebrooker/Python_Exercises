"""
Ezra S. Brooker

2021-07-30

Daily Coding Problem

You are given an array of non-negative integers that represents a two-
dimensional elevation map where each element is unit-width wall and the
integer is the height. Suppose it will rain and all spots between two
walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time
and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in
the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units of water in
first index, 2 in the second, and 3 in the fourth index (we cannot hold
5 since it would run off to the left), so we can trap 8 units of water.

Note: Took a hint from GeeksForGeeks.org to help uncover the second half
of the algorithm presented here. Was pretty obvious after the fact on how
to account for an ending wall that was lower than the previous wall...

"""


def trapped_water(elevations):

    units = 0
    temps = 0
    wall  = elevations[0]
    iwall = 0

    # Scan wall height differences to determine trapped
    # water from left to right
    for i in range(1,len(elevations)):

        if elevations[i] >= wall:
            iwall  = i
            wall   = elevations[i]
            temps  = 0
        else:
            temps += wall - elevations[i]
            units += wall - elevations[i]

    # Subtract out temp value if final wall is smaller than last wall
    # Work backwards to figure out trapped water with lower wall height
    if (iwall < len(elevations) - 1):

        units -= temps
        wall   = elevations[-1]
        for i in range(len(elevations)-1,iwall-1,-1):

            if (elevations[i] >= wall):
                wall = elevations[i]
            else:
                units += wall - elevations[i]

    return units


if __name__ == "__main__":

    h = [2, 0, 1]
    print( trapped_water(h), h )
    h = [0, 2, 1]
    print( trapped_water(h), h )
    h = [2, 1, 0]
    print( trapped_water(h), h )
    h = [2, 1, 2]
    print( trapped_water(h), h )
    h = [3, 0, 1, 3, 0, 5]
    print( trapped_water(h), h )
    h = [3, 0, 1, 3, 0, 2]
    print( trapped_water(h), h )
