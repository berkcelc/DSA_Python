def max_product(arr):
    """
    Find the maximum product of two numbers in an array.

    Parameters:
        arr (list): A list of integers.

    Returns:
        int: The maximum product of two numbers in the array.
    """
    max1, max2 = 0,0

    for num in arr:

        if num > max1:
            max2 = max1
            max1 = num

        elif num > max2:
            max2 = num

    return max1 * max2


max_product([3,2,9,5])

# Time complexity - O(n)
# Space Complexity - O(1)

# if we return a new list that is made as per the old list
# the space complexity will be O(n)


len([[1,2,3],[4,5,6],[7,8,9]])


# get the two largest numbers in a list

sam_list = [23, 43, 54, 89, 76]

def get_two_largest(nums):
    max1, max2 = 0,0

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max1, max2

get_two_largest(sam_list)


# removing the duplicates

sam_list = [1,1,4,4,5,6,7,8,8,5]

def rem_duplicates(arr):

    uniq = []
    seen = set()

    for i in arr:
        if i not in seen:
            uniq.append(i)
            seen.add(i)
    return uniq

rem_duplicates(sam_list)

def pair_sum(myList, sum):
    """
    Given a list of integers `myList` and a target sum `sum`, the function `pair_sum` finds all pairs of numbers in `myList` that add up to `sum` and returns them as a list of strings.

    Parameters:
    - `myList` (list): A list of integers.
    - `sum` (int): The target sum.

    Returns:
    - `los` (list): A list of strings representing pairs of numbers that add up to `sum`. Each string in the list is formatted as "{num1}+{num2}", where `num1` and `num2` are the numbers in a pair.

    Example:
    ```python
    >>> pair_sum([1, 2, 3, 4, 5], 6)
    ['2+4', '3+3']
    ```
    """
    seen = {}
    los = []
    for i, num in enumerate(myList):
        _com = sum - num
        if _com in seen:
            los.append(f'{_com}+{myList[i]}')
        seen[num] = i
    return los




# check duplicates

def contains_duplicates(nums):
    """
    Check if a list of numbers contains any duplicates.

    Parameters:
        nums (List[int]): A list of integers.

    Returns:
        bool: True if the list contains duplicates, False otherwise.
    """
    visited = set()
    for num in nums:
        if num in visited:
            return True
        visited.add(num)
    return False

