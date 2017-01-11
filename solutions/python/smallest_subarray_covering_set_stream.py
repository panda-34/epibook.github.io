from linked_list_prototype import LinkedList


# @include
def find_smallest_subarray_covering_subset(sin, query_strings):
    # Tracks the last occurrence (index) of each string in query_strings.
    loc = LinkedList()
    d = {s: None for s in query_strings}
    res = (-1, -1)
    for idx, s in enumerate(sin):
        if s in d:  # s is in query_strings.
            it = d[s]
            if it is not None:
                # Explicitly remove s so that when we add it, it's the string most
                # recently added to loc.
                loc.erase(it)
            loc.emplace_back(idx)
            d[s] = loc.end()

            if len(loc) == len(query_strings):
                # We have seen all strings in query_strings, let's get to work.
                if res == (-1, -1) or idx - loc.front() < res[1] - res[0]:
                    res = (loc.front(), idx)
    return res
# @exclude
