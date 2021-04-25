print(' ㅡㅡㅡ BOOK: Python Algorithm Interview ㅡㅡㅡ')

import collections
from typing import List


def majorityElement( nums: List[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a =  majorityElement(nums[:half])
    b =  majorityElement(nums[half:])
    r = [b, a][nums.count(a) > half]
    return r

c = [2,1,2]
# c = [2,2,2,1,2,2,1]
# #c = [1,2,2]
d=majorityElement(c)

print(d)
