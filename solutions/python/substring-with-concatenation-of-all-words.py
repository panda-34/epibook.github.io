# substring-with-concatenation-of-all-words.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import collections


# @include
def find_all_substrings(s, words):
    word_to_freq = collections.Counter(words)
    unit_size = len(words[0])
    result = []
    for i in range(len(s) - unit_size * len(words) + 1):
        if match_all_words_in_dict(s, word_to_freq, i, len(words), unit_size):
            result.append(i)
    return result


def match_all_words_in_dict(s, word_to_freq, start, num_words, unit_size):
    curr_string_to_freq = collections.Counter()
    for i in range(start, start + num_words * unit_size, unit_size):
        curr_word = s[i : i + unit_size]
        it = word_to_freq[curr_word]
        if it == 0:
            return False
        curr_string_to_freq[curr_word] += 1
        if curr_string_to_freq[curr_word] > it:
            # curr_word occurs too many times for a match to be possible.
            return False
    return True
# @exclude


def small_test():
    s = 'barfoothefoobarman'
    result = find_all_substrings(s, ['foo', 'bar'])
    assert result == [0, 9]
    s = 'dcacdabcd'
    result = find_all_substrings(s, ['cd', 'ab'])
    assert result == [3, 5]


def main():
    small_test()


if __name__ == '__main__':
    main()
