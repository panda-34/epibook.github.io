# Team_photo_1.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import collections

# @include
Player = collections.namedtuple('Player', ('height'))


class Team:
    def __init__(self, height):
        self._players = [Player(h) for h in height]

    # Checks if A can be placed in front of B.
    @staticmethod
    def valid_placement_exists(A, B):
        return all(a < b
                   for a, b in zip(A._sort_players_by_height(),
                                   B._sort_players_by_height()))

    def _sort_players_by_height(self):
        return sorted(self._players)


# @exclude


def main():
    height = [1, 5, 4]
    t1 = Team(height)
    height = [2, 3, 4]
    t2 = Team(height)
    assert not Team.valid_placement_exists(
        t1, t2) and not Team.valid_placement_exists(t2, t1)
    height = [0, 3, 2]
    t3 = Team(height)
    assert Team.valid_placement_exists(
        t3, t1) and not Team.valid_placement_exists(
            t1, t3) and Team.valid_placement_exists(
                t3, t2) and not Team.valid_placement_exists(t1, t2)
    height = [1, 4, 2]
    t4 = Team(height)
    assert not Team.valid_placement_exists(
        t4, t3) and not Team.valid_placement_exists(t3, t4)


if __name__ == '__main__':
    main()
