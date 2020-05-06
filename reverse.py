from sys import argv

from stack import LinkedStack


def reverse(num):
    str_num = str(num)
    stack = LinkedStack(list(str_num))
    reversed_num = ""
    while not stack.is_empty():
        reversed_num += stack.pop()
    return int(reversed_num)


if __name__ == '__main__':
    if len(argv) > 1:
        if argv[1].isdigit():
            print(f"{argv[1]} reversed is {reverse(int(argv[1]))}")
        else:
            print(f"12345 reversed is {reverse(12345)}")
    else:
        print(f"12345 reversed is {reverse(12345)}")
