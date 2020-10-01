def binary_search(data: list, low: int, high: int, target):
    """Return the index of target item. The list must be in sorted order."""
    try:
        if high >= low:
            mid = (high+low) // 2

            if data[mid] == target:
                return mid

            elif data[mid] > target:
                return binary_search(data, 0, mid-1, target)

            else:
                return binary_search(data, mid+1, len(data)-1, target)
        return -1

    except RecursionError:
        return "Please sort the list before passing it to function."
