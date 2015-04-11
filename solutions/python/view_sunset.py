# View_sunset.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


# @include
def examine_buildings_with_sunset(it):
    # Stores (building_idx, building_height) pair with sunset views.
    candidates = []
    for building_idx, building_height in enumerate(it):
        while candidates and building_height >= candidates[-1][1]:
            candidates.pop()
        candidates.append((building_idx, building_height))

    buildings_with_sunset = []
    while candidates:
        buildings_with_sunset.append(candidates.pop()[0])
    return buildings_with_sunset
# @exclude


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        heights = [random.randint(1, 2 * n) for i in range(n)]
        res = examine_buildings_with_sunset(iter(heights))
        print(res[0], heights[res[0]])
        for i in range(1, len(res)):
            print(res[i], heights[res[i]])
            assert heights[res[i - 1]] < heights[res[i]]


if __name__ == '__main__':
    main()
