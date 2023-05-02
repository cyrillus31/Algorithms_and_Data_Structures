""" Sliding window method"""


def binary_search_iteration(l: list, target):
    left = 0
    right = len(l)

    while left != right:
        mid = (right + left) // 2
        if target == l[mid]:
            return mid
        if target < l[mid]:
            right = mid
        else:
            left = mid + 1

def binary_search_recursion(l: list , target, left, right):
    if left == right:
        return None
    mid = (left + right) // 2
    if target == l[mid]:
        return mid
    if target < l[mid]:
        right = mid
    else:
        left = mid + 1
    return binary_search_recursion(l, target, left, right)

l = [1,2,3,4,5,6,7,8,9]
print(binary_search_iteration(l, 4))
print(binary_search_recursion(l, 0, 0, len(l)))
