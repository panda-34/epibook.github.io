# Search_maze.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import collections

# @include
WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    path = [s]
    maze[s.x][s.y] = BLACK
    if not search_maze_helper(s, e, maze, path):
        del path[-1]
    return path  # Empty path means no path between s and e.


# Perform DFS to find a feasible path.
def search_maze_helper(cur, e, maze, path):
    if cur == e:
        return True

    for s in (0, 1), (0, -1), (1, 0), (-1, 0):
        next = Coordinate(cur.x + s[0], cur.y + s[1])
        if is_feasible(next, maze):
            maze[next.x][next.y] = BLACK
            path.append(next)
            if search_maze_helper(next, e, maze, path):
                return True
            del path[-1]
    return False


# Checks cur is within maze and is a white pixel.
def is_feasible(cur, maze):
    return 0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[
        cur.x][cur.y] == WHITE


# @exclude


def main():
    for times in range(1000):
        if len(sys.argv) == 3:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
        else:
            n = random.randint(1, 30)
            m = random.randint(1, 30)
        maze = [[random.randrange(2) for j in range(m)] for i in range(n)]
        white = []
        for i in range(n):
            for j in range(m):
                if maze[i][j] == WHITE:
                    white.append(Coordinate(i, j))
            print(*maze[i])
        print()
        if white:
            start = random.randrange(len(white))
            end = random.randrange(len(white))
            print(white[start].x, white[start].y)
            print(white[end].x, white[end].y)
            path = search_maze(maze, white[start], white[end])
            if path:
                assert white[start] == path[0] and white[end] == path[-1]
            for i in range(len(path)):
                if i > 0:
                    assert abs(path[i - 1].x - path[i].x) + abs(path[i - 1].y -
                                                                path[i].y) == 1
                print('(%d,%d)' % path[i])


if __name__ == '__main__':
    main()
