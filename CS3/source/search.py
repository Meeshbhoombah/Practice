#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index == len(array):
        return None

    if item == array[index]:
        return index

    linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    start_index = 0
    stop_index = len(array) - 1

    while start_index <= stop_index:
        split_index = int((start_index + stop_index) / 2)

        if array[split_index] == item:
            return split_index
        else:
            if item < array[split_index]:
                stop_index = split_index - 1
            else:
                start_index = split_index + 1


def binary_search_recursive(array, item):
    # implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if len(array) == 0:
        return 
    else:
        split = len(array) // 2
        
        if array[midpoint] == item:
            return True	        
        else:
            if item < array[split]:
                return binary_search_recursive(array[:midpoint], item)
            else:
                return binary_search_recursive(array[midpoint + 1:], item)
	

