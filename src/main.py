from dataclasses import dataclass, Field

sample_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

full_data_file = "full_data.txt"
# Get to something like:
# {
#     (x, y): 1 -> 2 ->3
# }

# 0, 9 -> 5, 9: {(0, 9): 1, (1, 9): 1}
# (0,9): 2

def parse_endpoints(line):
    # "8,0 -> 0,8"
    coord1, coord2 = line.split(" -> ")

    x1, y1 = coord1.split(",")

    x2, y2 = coord2.split(",")

    return (
        (int(x1), int(y1)), (int(x2), int(y2)),
    )


def parse_lines(text_data):
    lines = text_data.split("\n")

    return lines


def get_keys(endpoint_pair):
    """
    Returns the list of points covered by a
    horizontal or vertical line described by endpoints

    (Returns empty list if not a horizontal or vertical
    line!)
    """
    (x1, y1), (x2, y2) = endpoint_pair
    is_horizontal = True if x1 == x2 else False
    is_vertical = True if y1 == y2 else False
    keys_list = []
    if is_horizontal:
        start = min(y1, y2)
        end = max(y1, y2)
        for yn in range(start, end+1):
            keys_list.append((x1, yn))
    if is_vertical:
        start = min(x1, x2)
        end = max(x1, x2)
        for xn in range(start, end+1):
            keys_list.append((xn, y1))
    return keys_list


def map_keys(keys, map_dict):
    """
    Given a list of keys/lines, map them into a dict,
    counting the number of keys per point as an int
    """
    for key in keys:
        if key in map_dict:
            map_dict[key] += 1
        else:
            map_dict[key] = 1
    return map_dict


if __name__ == "__main__":
    # read from file
    # turn into lines - done
    # turn into coords - done
    # filter for horiz/vertical lines - done (sort of)
    # turn into keys/lines - done
    # count the keys - done
    with open(full_data_file, 'r') as f:
        full_data = f.read()

    lines = parse_lines(full_data)

    endpoint_pairs = [parse_endpoints(line) for line in lines]

    key_lists = [get_keys(pair) for pair in endpoint_pairs]

    counts = {}
    for keys in key_lists:
        map_keys(keys, counts)

    # print(counts)

    multis = [value for value in counts.values() if value > 1]

    print("Multis:", len(multis))