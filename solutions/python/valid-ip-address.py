# valid-IP-address.cc 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys


# @include
def get_valid_IP_address(s):
    result = []
    for i in range(1, min(4, len(s))):
        first = s[:i]
        if is_valid_part(first):
            for j in range(1, min(len(s) - i, 4)):
                second = s[i : i + j]
                if is_valid_part(second):
                    for k in range(1, min(len(s) - i - j, 4)):
                        third = s[i + j : i + j + k]
                        fourth = s[i + j + k :]
                        if is_valid_part(third) and is_valid_part(fourth):
                            result.append('.'.join((first, second, third, fourth)))
    return result


def is_valid_part(s):
    if len(s) > 3:
        return False
    # '00', '000', '01', etc. are not valid, but '0' is valid.
    if s[0] == '0' and len(s) > 1:
        return False
    val = int(s)
    return 0 <= val <= 255
# @exclude


def main():
    if len(sys.argv) == 2:
        result = get_valid_IP_address(sys.argv[1])
        for s in result:
            print(s)
    res1 = get_valid_IP_address('255255255255')
    for s in res1:
        print(s)
    res2 = get_valid_IP_address('19216811')
    for s in res2:
        print(s)


if __name__ == '__main__':
    main()
