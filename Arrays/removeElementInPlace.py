"""
Follow up questions: How could this have been different if it was not in place?
 Learn more two pointer Algorithms Questions Here: https://leetcode.com/tag/two-pointers/
"""


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    ## remove the element:
    # [3,2,2,3] -> [3,3

    pos = 0 # This is the position to put the element not equal to the given target (which needs to be removed)
    for i in range(len(nums)):
        if nums[i] != val:
            nums[pos] = nums[i]
            pos += 1
    print(nums[:pos])
    return len(nums[:pos])


print(removeElement([2,2,2,2,3,4,5],2))