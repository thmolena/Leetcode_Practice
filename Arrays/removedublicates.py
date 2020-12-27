def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # [1,1,2,3,4,4,5]
    # have 2 pointers moving ->
    # the first is comparing items, the second is inserting them at right positions

    # [1,2,2,2,3,4,4,5] -->
    print("given nums",nums)
    if len(nums) <= 1:
        return len(nums)
    prev=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[prev]=nums[i]
            prev+=1
    print("modified nums",nums)
    print("final solution",nums[:prev])
    return len(nums[:prev])


print(removeDuplicates([1,1,2,2,3,3,4,5,6]))

# follow up questin: return length, return the array itself.
