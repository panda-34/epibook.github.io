# Replace_and_remove.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def replace_and_remove(s):
    # Use list of characters as a mutable string.
    s = s.copy()
    # Forward iteration: remove 'b's and count the number of 'a's.
    write_idx = 0
    a_count = 0
    for c in s:
        if c != 'b':
            s[write_idx] = c
            write_idx += 1
        if c == 'a':
            a_count += 1

    # Allocates space according to the number of 'a'.
    new_len = write_idx + a_count
    if new_len > len(s):
        s += [''] * (new_len - len(s))
    else:
        del s[new_len:]
    # Backward iteration: replace "a"s with "dd"s starting from the end.
    cur_idx = write_idx - 1
    write_idx = -1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx] = 'd'
            write_idx -= 1
            s[write_idx] = 'd'
            write_idx -= 1
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return s
# @exclude


def rand_string(length):
    ret = [random.choice('abcd') for i in range(length)]
    return ret


def check_ans(s, ans):
    temp = []
    for i in s:
        if i == 'a':
            temp += ['d', 'd']
        elif i != 'b':
            temp.append(i)
    assert ans == temp


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            s = list(sys.argv[1])
        else:
            s = rand_string(random.randint(1, 1000))
        print(''.join(s))
        ans = replace_and_remove(s)
        print(''.join(ans))
        print()
        check_ans(s, ans)


if __name__ == '__main__':
    main()
