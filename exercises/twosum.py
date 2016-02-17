'''
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target and nums[i] != nums[j]:
                return [i, j]
'''

def twoSum(nums, target):
    mapping = {}
    for i in range(len(nums)):
        if nums[i] in mapping:
            return [mapping[nums[i]], i]
        else:
            sec_num = target - nums[i]
            mapping[sec_num] = i

