# surrounded-regions.cc 884568f491146065472fafc32923e8aa73dd8076
import sys
import random
import collections


# @include
def fill_surrounded_regions(board):
    if not board:
        return

    visited = [[False] * len(board[0]) for _ in board]
    # Identifies the regions that are reachable via white path starting from the first or last columns.
    for i in range(len(board)):
        if board[i][0] == 'W' and not visited[i][0]:
            mark_boundary_region(i, 0, board, visited)
        if board[i][-1] == 'W' and not visited[i][-1]:
            mark_boundary_region(i, len(board[i]) - 1, board, visited)
    # Identifies the regions that are reachable via white path starting from the first or last rows.
    for j in range(len(board[0])):
        if board[0][j] == 'W' and not visited[0][j]:
            mark_boundary_region(0, j, board, visited)
        if board[-1][j] == 'W' and not visited[-1][j]:
            mark_boundary_region(len(board) - 1, j, board, visited)

    # Marks the surrounded white regions as black.
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[i]) - 1):
            if board[i][j] == 'W' and not visited[i][j]:
                board[i][j] = 'B'


def mark_boundary_region(i, j, board, visited):
    Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
    q = collections.deque()
    q.append(Coordinate(i, j))
    visited[i][j] = True
    # Uses BFS to traverse this region.
    while q:
        curr = q.popleft()
        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            next = Coordinate(curr.x + d[0], curr.y + d[1])
            if (0 <= next.x < len(board) and 0 <= next.y < len(board[next.x])
                    and board[next.x][next.y] == 'W' and
                    not visited[next.x][next.y]):
                visited[next.x][next.y] = True
                q.append(next)


# @exclude


def simple_test():
    A = [['B', 'B', 'B', 'B'], ['W', 'B', 'W', 'B'], ['B', 'W', 'W', 'B'],
         ['B', 'B', 'B', 'B']]
    fill_surrounded_regions(A)
    golden = [['B', 'B', 'B', 'B'], ['W', 'B', 'B', 'B'],
              ['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]
    assert A == golden


def main():
    simple_test()
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    else:
        n = random.randint(1, 1000)
        m = random.randint(1, 1000)
    board = [[random.choice(('B', 'W')) for j in range(m)] for i in range(n)]
    for row in board:
        print(*row, sep='')
    fill_surrounded_regions(board)
    print()
    for row in board:
        print(*row, sep='')


if __name__ == '__main__':
    main()
