import flatten

def test_flatten():
    assert flatten.flatten(1) == [1]
    assert flatten.flatten((1,)) == [1]
    assert flatten.flatten([1]) == [1]
    assert flatten.flatten({1}) == [1]
    assert flatten.flatten(None) == [None]
    assert flatten.flatten([1, [2, (3,)], [[[[[[4, 5]]]]], 6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten.flatten({"dict": 1}) == [{"dict": 1}]


