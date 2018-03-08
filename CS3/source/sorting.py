#!python

from binarytree import BinarySearchTree

def is_sorted(items):
    """ Return a boolean indicating whether given items are in ascending order

    Checks if items contains any values. If it does, returns False, or not sorted, when
    a greater value appears before a lesser value.

    Args:
        - items (list): a list of unsorted items

    Returns:
        - sorted_check (boolean): returns true if the items are in ascending order,
          false if otherwise
    """
    if items:
        for i in range(0, len(items)):
            try:
                # not sorted if a greater values appears 
                # prior to a smaller (out of order)
                if items[i] > items[i + 1]:
                    return False

            except IndexError:
                # items list bound reached with no item
                # out of order
                return True
    else:
        # empty list sorted vacuously
        return True 

            
def bubble_sort(items):
    """ Sort items by swapping adjacent pairs of items that are in the wrong order.

    Passes through list until no swaps are needed, in which case the list is sorted. The
    inner loop can ignore the last value beacuse the n-th pass finds the n-th largest value
    and puts it in its final place.
    
    + Runtime Time:
      Worst case: O(n^2)
      Avg case: O(n^2) 
      
    + Memory:
      O(1) - no need to allocate memory for any of the items

    Args:
        - items (list): a list of unsorted items
    
    Returns:
        - sorted_items (list): the passed list, sorted
    """
    # can ignore looking at the last value each time
    for delimiter in range(len(items) - 1, 0, -1):
        for i in range(delimiter):
            print(items)
            # greater value appears before smaller value
            if items[i] > items[i + 1]:
                # swap
                items[i], items[i + 1] = items[i + 1], items[i]


def selection_sort(items):
    """
    got heem
    """
    return "Got heem"


def insertion_sort(items):
    """
    re:factoring
    """
    for i in range(1, len(items)):

        current_value = items[i]
        current_pos = i

        while current_pos > 0 and items[current_pos - 1] > current_value:
            items[current_pos] = items[current_pos - 1]
            current_pos = current_pos - 1

        items[current_pos] = current_value


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """ Sorts a list in place, rescursively, splitting lists into sublists then merging them

    Divides the unsorted list into N lists (where N = number of items in the collection),
    each of which contain one element, which is considered sorted. Then merges those
    sublists.

    Args:
        - items (list): a collection of items, sored or unsorted

    Returns:
        - None (None): sorts collection in place
    """
    # lists with one element are sorted and should trigger the merge sequence
    if len(items) > 1:
        """
        Split
        """

        split_index =  len(items) // 2

        left = items[:split_index]
        right =  items[split_index:]

        # rescursively call merge_sort on the two halves
        merge_sort(left)
        merge_sort(right)

        """
        Merge
        """

        # i and j serve as counters for left and right respectively (avoid IndexErrors)
        # k is the index at which an item should be inserted after comparisons are made
        i, j, k = 0, 0, 0

        # both left and right have not been completly iterated through
        while i < len(left) and j < len(right):

            # determine the greater value and insert into the array
            # then increment the counter from which the item was removed
            # and recompare
            if left[i] < right[j]:
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j += 1
        
            k += 1

        # completely iterated through right but items remain in left
        while i < len(left):
            items[k] = left[i]
            i += 1
            k += 1

        ## completely iterated through items but items remain in right
        while j < len(right):
            items[k] = right[j]
            j += 1
            k += 1

def tree_sort(items):
    """ Uses a binary serach tree to sort a list of items
    """
    sorted_items = BinarySearchTree(items)
    items[:] = sorted_items.items_in_order()





def quick_sort(items, pivot_index = 0, pivot_right = 1):
    """ Refactoring """

    items = items[:]
    
    if not is_sorted(items):

        print(items)

        pivot_index = 0
        pivot_right = pivot_index + 1

        # subtract one for index
        for index in range(pivot_index, len(items) - 1):

            if items[index] < items[pivot_index]:

                index, pivot_right = pivot_right, index

                pivot_right += 1
            
            pivot_index, pivot_right = pivot_right, pivot_index

            print(items)

        quick_sort(items, pivot_index, pivot_right)

def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
