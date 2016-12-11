# Missing_element.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import os


# @include
def find_missing_element(ifs):
    NUM_BUCKET = 1 << 16
    counter = [0] * NUM_BUCKET
    for x in map(int, ifs):
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    # Look for a bucket that contains less than (1 << 16) elements.
    BUCKET_CAPACITY = 1 << 16
    for i in range(NUM_BUCKET):
        if counter[i] < BUCKET_CAPACITY:
            candidate_bucket = i
            break

    # Finds all IP addresses in the stream whose first 16 bits are equal to candidate_bucket.
    ifs.seek(0)
    bit_vec = [0] * BUCKET_CAPACITY
    for x in map(int, ifs):
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # Records the presence of 16 LSB of x.
            lower_part_x = ((1 << 16) - 1) & x
            bit_vec[lower_part_x] = 1

    # At least one of the LSB combinations is absent, find it.
    for i in range(BUCKET_CAPACITY):
        if bit_vec[i] == 0:
            return (candidate_bucket << 16) | i

# @exclude
    raise ValueError('no missing element')


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 300000000
    hash = set()
    with open('missing.txt', 'w') as ofs:
        for i in range(n):
            hash.add(i)
            ofs.write(str(i))
            ofs.write('\n')
    with open('missing.txt') as ifs:
        print('Before finding missing')
        missing = find_missing_element(ifs)
        assert missing not in hash
    # Remove file after the execution.
    os.remove('missing.txt')
    print(missing)


if __name__ == '__main__':
    main()
