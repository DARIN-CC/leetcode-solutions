# LeetCode 1 - Two Sum
# Difficulty: Easy

solution:用两个指针往后遍历,寻找符合条件的组合.

双重循环时间复杂度n^2


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)

        return result


#New!!!使用哈希表


时间复杂度n,空间复杂度变高了
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdic={}
        for i,num in enumerate(nums):
            need = target-num
            if need in hashdic:
                return [hashdic[need],i]
            hashdic[num]=i
