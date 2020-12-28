#!/usr/bin/env python3

import heapq
import typing
import argparse


# read a list of ints from the passed-in file and then print out the greatest
# K ints from that file.

# example usage:
# python3 topk.py -k 3 my_file_full_of_ints.txt

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    parser.add_argument('-k', type=int)
    args = parser.parse_args()
    with open(args.filename) as fp:
        h = scan_file(fp, args.k)
    print(h)


def scan_file(fp: typing.IO, k: int) -> typing.List[int]:
    h: typing.List[int] = []  # the heap of the top-K elements
    for line in fp:
        try:
            push(h, int(line), k)
        except ValueError:
            continue

    # we're only sorting the top-K once at the end so this sort is O(N*log(N)) where N == k
    # (and k is presumably quite small).  In the degenerate case where k is extremely large,
    # this sort would probably eat up all available memory, but then storing all the values
    # in the (degenerately large) heap would already have done that by this point.
    return sorted(h, reverse=True) 


# keep track of the most recent value to "fall out" of the heap.  We know for sure that
# any new value read from the file which is less than this value cannot be in the top-K
too_small = None 


# whenever the top-K heap is changed, update a set representation of the heap so that
# it is O(1) to check if a number is already in the top-K and to therefore avoid adding
# a dupe.  It is O(N) to re-create the set whenever this happens, but N in this case is k,
# and therefore presumably small. The alternative to this would be to perform an O(log(N))
# membership lookup in the heap for every insert but we're betting that this lookup happens
# frequently enough (and that updates to the top-K heap happens infrequently enough) 
# to make the O(N) set creation worth it so that subsequent membership lookup is O(1)
# instead of O(log(N))
# Assuming the ordering of the numbers is anything even slightly better than the worst case
# (which would be if the numbers are already sorted), we'll win this bet.  
# If we wanted to handle this worst case, we could get super fancy by seek()ing around in the
# file randomly to guarantee a level of randomness to the ordering. But I'm not going to
# do that.
h_set = set()

def push(h: list, val: int, k: int) -> None:
    """
    
    """
    global too_small
    global h_set

    # if a value that's less than (or equal to) this value has already "fallen out" of the
    # top-K heap, we know that this value will not be big enough to land in there and we
    # can return early
    if too_small is not None and val <= too_small:
        return

    # if this value is large enough to be in the set but its value already appears there,
    # avoid adding a dupe and return early
    if val in h_set:
        return

    heapq.heappush(h, val)

    # if the most recent heappush() caused our heap to exceed K, then drop the smallest
    # element and record that value in too_small in order to quickly skip any values
    # in the future that are too small to end up in the top-K heap.
    if len(h) > k:
        too_small = heapq.heappop(h)

    
    # maintain the set representation of this heap that lets us avoid adding dupes in
    # O(1) time
    h_set = set(h)


if __name__ == '__main__':
    main()
