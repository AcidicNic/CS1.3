#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # return contains_iterative(text, pattern)
    return contains_recursive(text, pattern)


def contains_iterative(text, pattern):
    ''' looks for each substring of text that is the length of the pattern, returns true if the pattern has a match. '''
    for i in range(0, len(text)-len(pattern)+1):
        if pattern == text[i:i+len(pattern)]:
            return True
    return False


def contains_recursive(text, pattern, index=0):
    ''' same as idea as iterative, but it's done recursively! '''
    if index < len(text)-len(pattern)+1:
        if pattern == text[index:index+len(pattern)]:
            return True
        return contains_recursive(text, pattern, index+1)
    else:
        return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # return find_index_iterative(text, pattern)
    return find_index_recursive(text, pattern)


def find_index_iterative(text, pattern):
    for i in range(0, len(text)-len(pattern)+1):
        if pattern == text[i:i+len(pattern)]:
            return i
    return None


def find_index_recursive(text, pattern, index=0):
    if index < len(text)-len(pattern)+1:
        if pattern == text[index:index+len(pattern)]:
            return index
        return find_index_recursive(text, pattern, index+1)
    else:
        return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # return find_all_iterative(text, pattern)
    return find_all_recursive(text, pattern)


def find_all_iterative(text, pattern):
    if pattern == '':
        return [*range(0, len(text))]

    indexes = []
    for i in range(0, len(text)-len(pattern)+1):
        if pattern == text[i:i+len(pattern)]:
            indexes.append(i)
    return indexes


def find_all_recursive(text, pattern, indexes=None, index=0):
    if pattern == '':
        return [*range(0, len(text))]
    if indexes is None:
        indexes = []

    for i in range(0, len(text) - len(pattern) + 1):
        if pattern == text[i:i + len(pattern)]:
            indexes.append(i)
    return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    print(f"'nicoleisrad' contains 'rad' at index: {find_index_recursive('nicoleisrad!!', 'rad')}")
