from random import randint
from io import StringIO

import maxk

def test_garbage_input():
    """
    max-K script doesn't blow up when encountering non-integer lines in its input file
    """

    test_fp = StringIO("""

        😀
        asdf
        one
        two
        three
        1
        2
        3""")

    assert maxk.scan_file(fp=test_fp, k=3) == [3, 2, 1]

def test_negative_values():
    """
    max-K script correctly sorts negative values
    """

    test_fp = StringIO("""
        -1
        -2
        -3
        -4
        -5
        """)
    assert maxk.scan_file(fp=test_fp, k=3) == [-1, -2, -3]


def test_randoms():
    """
    max-K script yields same result as manually sorting and picking top-K values
    """ 
    randlist = [randint(-2 ** 32, 2 ** 32) for _ in range(10000)]
    test_fp = StringIO("\n".join(str(i) for i in randlist))

    assert maxk.scan_file(fp=test_fp, k=3) == sorted(randlist, reverse=True)[:3]
