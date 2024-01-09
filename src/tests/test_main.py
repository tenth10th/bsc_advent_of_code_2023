from src.main import (
    sample_data, parse_endpoints, parse_lines, get_keys,
    map_keys,
)


def test_parse_endpoints():
    coordinates = parse_endpoints("8,0 -> 0,8")

    assert coordinates == (
        (8, 0), (0, 8)
    )

def test_parse_lines():
    lines =  parse_lines(sample_data)

    assert lines[0] == "0,9 -> 5,9"
    assert len(lines) == 10

def test_get_keys():
    coordinate = ((0, 9), (5, 9))
    keys = get_keys(coordinate)
    assert keys == [
        (0, 9),
        (1, 9),
        (2, 9),
        (3, 9),
        (4, 9),
        (5, 9),
    ]

def test_get_keys_ignores():
    coordinate = ((8, 0), (0, 8))
    keys = get_keys(coordinate)
    assert keys == []


def test_map_keys():
    map_dict = {}
    keys = [
        (0, 9),
        (1, 9),
        (2, 9),
        (3, 9),
        (4, 9),
        (5, 9),
    ]
    expected_dict = map_keys(keys, map_dict)
    assert expected_dict == {
        (0, 9): 1,
        (1, 9): 1,
        (2, 9): 1,
        (3, 9): 1,
        (4, 9): 1,
        (5, 9): 1,
    }


def test_map_keys_with_addition():
    map_dict = {
        (0, 9): 1,
        (1, 9): 1,
    }
    keys = [
        (1, 9),
    ]
    expected_dict = map_keys(keys, map_dict)
    assert expected_dict == {
        (0, 9): 1,
        (1, 9): 2,
    }


def test_sample_data():
    lines = parse_lines(sample_data)
    endpoint_pairs = [parse_endpoints(line) for line in lines]
    key_lists = [get_keys(pair) for pair in endpoint_pairs]
    counts = {}
    for keys in key_lists:
        map_keys(keys, counts)
    print(counts)
    twos = [value for value in counts.values() if value == 2]
    assert len(twos) == 5


# def test_failing_cases():
#     endpoint_pairs = [
#         ((9, 4), (3, 4)),
#         ((3, 4), (1, 4)),
#     ]
#     key_lists = [get_keys(pair) for pair in endpoint_pairs]
#     counts = {}
#     for keys in key_lists:
#         map_keys(keys, counts)
#     print("Counts:", counts)
#     twos = [value for value in counts.values() if value == 2]
#     print("twos:", twos)
#     assert len(twos) == 2
