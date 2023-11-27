def is_whole_div(num1, num2):
    return num1 % num2 == 0

def max_ocurrence(arr):
    occurrences = {num: arr.count(num) for num in set(arr)}
    return max(occurrences.values())

def max_occurrence_elements(arr):
    occurrences = {num: arr.count(num) for num in set(arr)}
    return sorted([num for num, count in occurrences.items() if count == max(occurrences.values())])

def once_occurrence_amount(arr):
    return len([x for x in set(arr) if arr.count(x) == 1])
def stat(arr):
    if not isinstance(arr, list) or not arr or any(isinstance(x, float) for x in arr):
        return [0, 0, 0, [], 0]

    total_amount = len(arr)
    unique_amount = len(set(arr))
    once_occ_amount = once_occurrence_amount(arr)

    max_occ = max_ocurrence(arr)
    max_occ_elem = max_occurrence_elements(arr)

    result = [total_amount, unique_amount, once_occ_amount, max_occ_elem, max_occ]
    return result