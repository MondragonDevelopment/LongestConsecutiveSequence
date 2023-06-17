nums = [100,4,200,1,3,2]
nums1 = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):
    Set = set(nums)
    longest = 0
    for i in range(len(nums)):
        current = nums[i]
        if current - 1 not in Set:
            length = 1
            while current + length in Set:
                length += 1
            longest = max(length, longest)
    return longest

print(longestConsecutive(nums1))