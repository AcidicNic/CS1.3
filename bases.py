# !python
import string
import re


def get_set(base):
    """creates string that contains all of the valid characters for the given base
        base: int -- base for number
        return: str -- contains all of the valid characters for the given base"""
    all_chars = string.digits + string.ascii_lowercase
    set = "0"
    for i in range(base - 1):
        set += all_chars[i + 1]
    return set


def verify_digits(digits, base):
    """Verifies that the given digits only contain characters for the given base.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: bool -- True if the digits match the given base, otherwise False."""
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    set_for_base = get_set(base)
    if re.fullmatch(f'[{set_for_base}]+', str(digits).lower()):
        return True
    return False


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # verifies that digits only contains valid characters for the given base
    assert verify_digits(digits, base), f'{digits} contains invalid characters for base {base}'
    digits = str(digits).lower()
    decoded = 0
    base_set = get_set(base)
    place = 0
    # loops through each char in digits backwards
    for char in digits[::-1]:
        # loops through the set for the given base and looks for a character from the set that matches the current char
        for i in range(len(base_set)):
            if char == base_set[i]:
                # does the math to add the correct number in base 10 to add to the result
                decoded += (base ** place) * i
        place += 1
    return decoded


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # using this logic! --> https://www.youtube.com/watch?v=gvJYNAiwOhc
    base_set = get_set(base)
    result = ""
    while True:
        remainder = number % base
        number = number // base
        # find char for given base and add it to the result
        result += base_set[remainder]
        if number == 0:
            # reverse result str
            return result[::-1]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    if base1 == 10:
        result = encode(int(digits), base2)
    elif base2 == 10:
        result = decode(digits, base1)
    else:
        base_10 = decode(digits, base1)
        result = encode(int(base_10), base2)
    return str(result)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    print(get_set(16))
    b = string.digits + string.ascii_lowercase
    b = b[0:16]
    print(b)


    # num = 123456790
    # base = 36
    # print(f"{num} converted to base {base}: {encode(num, base)}")
    # num = 'hZ1d9s2'
    # print(f"{num} converted to decimal: {decode(num, base)}")
