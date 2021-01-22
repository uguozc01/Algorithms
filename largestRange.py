''' Write a function that takes in an array of integers and returns an array of 
length 2 representing the largest of integers contained in that array
The first number in the out put array should be the first number in the range.
A range of numbers is defined as a set of numbers that come right after each other
in the set of real integers. For instance, the output array [2,6] represents the
range {2,3,4,5,6}, which has a range of. Assume that there will be only one largest range
'''

# O(N) time | O(N) space
def largestRange(arr):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in arr:
        nums[num] = True
    for num in arr:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange
