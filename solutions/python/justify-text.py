# justify-text.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import math


# @include
def justify_text(words, L):
    curr_line_start = num_words_curr_line = curr_line_length = 0
    result = []
    for i, word in enumerate(words):
        # curr_line_start is the first word in the current line, and i is used to
        # identify the last word.
        num_words_curr_line += 1
        lookahead_line_length = curr_line_length + len(word) + (
            num_words_curr_line - 1)
        if lookahead_line_length == L:
            result.append(
                join_a_line_with_space(words, curr_line_start, i, i -
                                       curr_line_start))
            curr_line_start = i + 1
            num_words_curr_line = curr_line_length = 0
        elif lookahead_line_length > L:
            result.append(
                join_a_line_with_space(words, curr_line_start, i - 1, L -
                                       curr_line_length))
            curr_line_start = i
            num_words_curr_line = 1
            curr_line_length = len(word)
        else:  # lookahead_line_length < L.
            curr_line_length += len(word)

    # Handles the last line. Last line is to be left-aligned.
    if num_words_curr_line > 0:
        line = join_a_line_with_space(words, curr_line_start,
                                      len(words) - 1, num_words_curr_line - 1)
        line += ' ' * (L - curr_line_length - (num_words_curr_line - 1))
        result.append(line)
    return result


# Joins strings in words[start : end] with num_spaces spaces spread evenly.
def join_a_line_with_space(words, start, end, num_spaces):
    num_words_curr_line = end - start + 1
    line = []
    for i in range(start, end):
        line.append(words[i])
        num_words_curr_line -= 1
        num_curr_space = math.ceil(num_spaces / num_words_curr_line)
        line.append(' ' * num_curr_space)
        num_spaces -= num_curr_space
    line.append(words[end] + ' ' * num_spaces)
    return ''.join(line)


# @exclude


def test_case(words, L, golden):
    result = justify_text(words, L)
    for s in result:
        print("'%s'" % s)
    print()
    assert result == golden


def main():
    words = ['Text', 'justification', 'is', 'trickier', 'than', 'it', 'seems!']
    golden = [
        'Text          ', 'justification ', 'is    trickier', 'than it seems!'
    ]
    L = 14
    print('L =', L)
    test_case(words, L, golden)
    words = ['Listen', 'to', 'many,', 'speak', 'to', 'a', 'few.']
    golden = ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']
    L = 6
    print('L =', L)
    test_case(words, L, golden)
    words = [
        'The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy',
        'dogs.'
    ]
    golden = [
        'The   quick', 'brown   fox', 'jumped over', 'the    lazy',
        'dogs.      '
    ]
    L = 11
    print('L =', L)
    test_case(words, L, golden)
    golden = ['The  quick brown', 'fox  jumped over', 'the lazy dogs.  ']
    L = 16
    print('L =', L)
    test_case(words, L, golden)
    golden = ['The  quick  brown', 'fox  jumped  over', 'the lazy dogs.   ']
    L = 17
    print('L =', L)
    test_case(words, L, golden)
    words = ['Hello', 'World']
    golden = ['Hello World   ']
    L = 14
    test_case(words, L, golden)


if __name__ == '__main__':
    main()
