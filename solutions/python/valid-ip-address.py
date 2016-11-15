# valid-IP-address.cc 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys


# @include
def get_valid_IP_address(s):
    result = []
    for i in range(1, min(4, len(s))):
        first = s[:i]
        if is_valid_part(first):
            for j in range(1, min(len(s) - i, 4)):
                second = s[i:i + j]
                if is_valid_part(second):
                    for k in range(1, min(len(s) - i - j, 4)):
                        third, fourth = s[i + j:i + j + k], s[i + j + k:]
                        if is_valid_part(third) and is_valid_part(fourth):
                            result.append('.'.join((first, second, third,
                                                    fourth)))
    return result


def is_valid_part(s):
    if len(s) > 3:
        return False
    # '00', '000', '01', etc. are not valid, but '0' is valid.
    if s[0] == '0' and len(s) > 1:
        return False
    return 0 <= int(s) <= 255


# @exclude


def main():
    if len(sys.argv) == 2:
        result = get_valid_IP_address(sys.argv[1])
        for s in result:
            print(s)
    res1 = get_valid_IP_address('255255255255')
    assert res1 == ['255.255.255.255']
    res2 = get_valid_IP_address('19216811')
    assert len(res2) == 9
    res3 = get_valid_IP_address('1111')
    assert res3 == ['1.1.1.1']
    res4 = get_valid_IP_address('11000')
    assert len(res4) == 2
    sorted(res4)
    assert res4 == ['1.10.0.0', '11.0.0.0']


if __name__ == '__main__':
    main()
