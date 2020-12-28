#!/usr/bin/env python3


def main():
    a = [1, [2, (3,)], [[[[[[4]]]]], 5]]
    print(list(flatten(a)))


def flatten(thingy):
    if not isinstance(thingy, (list, tuple, set)):
        return [thingy]

    retval = []
    for e in thingy:
        retval += flatten(e)
    return retval
    


if __name__ == '__main__':
    main()
