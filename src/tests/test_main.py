from src.main import main, parse_line, load_lines_from_file
from pytest import mark

TEST_DATA = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet\
"""

TEST_LINES = TEST_DATA.split("\n")

# 12, 38, 15, and 77. Adding these together produces 142.
EXPECTED_VALUES = [12, 38, 15, 77]

EXPECTED_TOTAL = 142


def test_lines():
    for line in TEST_LINES:
        print(line)
    assert len(TEST_LINES) == 4


@mark.parametrize(
    ["line", "expected_number"],
    [
        ("1abc2", 12),
        ("1abc23", 13),
    ],
)
def test_first_line(line, expected_number):
    assert parse_line(line) == expected_number


def test_main():
    assert main(TEST_LINES) == EXPECTED_TOTAL


@mark.expensive
def test_main_full_data():
    lines = load_lines_from_file()
    assert main(lines) == 55_002
