#!python
import time


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array[index] == item:
        return index
    elif index + 1 >= len(array):
        return None
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    min = 0
    max = len(array)
    mid = -1

    while min <= max:
        prev_mid = mid
        mid = (max + min) // 2
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            min = mid
        else:
            max = mid
        if mid == prev_mid:
            return None


def binary_search_recursive(array, item, left=None, right=None):
    # if first loop.
    if left is None or right is None:
        left = 0
        right = len(array) -1

    # set midpoint and check if item has been found.
    mid = (left + right) // 2
    if array[mid] == item:
        return mid
    elif array[mid] < item:
        left = mid + 1
    else:
        right = mid - 1
    # check for infinite loop! (if old midpoint == next midpoint, it will continue to loop.)
    if mid == (left + right) // 2:
        return None
    else:
        return binary_search_recursive(array, item, left, right)