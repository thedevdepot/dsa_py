# Problem: Merge two sorted lists into a single sorted list

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    Args:
        list1 (list): First sorted list.
        list2 (list): Second sorted list.
    Returns:
        list: Merged sorted list.
    """
    merged = []
    i, j = 0, 0

    # Compare elements from both lists and add the smaller one to merged
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Add any remaining elements from list1
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # Add any remaining elements from list2
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

# Example usage:
if __name__ == "__main__":
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    result = merge_sorted_lists(a, b)
    print("Merged list:", result)
    # Output: Merged list: [1, 2, 3, 4, 5, 6, 7, 8, 10]