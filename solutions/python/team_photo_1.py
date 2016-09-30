# Team_photo_1.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# @include
class Player:
    def __init__(self, height):
        self.height = height

    def __lt__(self, other):
        return self.height < other.height


class Team:
    def __init__(self, height):
        self._players = [Player(h) for h in height]

    # Checks if A can be placed in front of B.
    @staticmethod
    def valid_placement_exists(A, B):
        A_sorted = A._sort_players_by_height()
        B_sorted = B._sort_players_by_height()
        for a, b in zip(A_sorted, B_sorted):
            if b < a:
                return False
        return True

    def _sort_players_by_height(self):
        return sorted(self._players)
# @exclude


def main():
    height = [1, 5, 4]
    t1 = Team(height)
    height = [2, 3, 4]
    t2 = Team(height)
    assert not Team.valid_placement_exists(t1, t2) and not Team.valid_placement_exists(t2, t1)
    height = [0, 3, 2]
    t3 = Team(height)
    assert (Team.valid_placement_exists(t3, t1) and
            not Team.valid_placement_exists(t1, t3) and
            Team.valid_placement_exists(t3, t2) and
            not Team.valid_placement_exists(t1, t2))


if __name__ == '__main__':
    main()
