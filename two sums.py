class Solution(object):
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers)-1
        while(i<j):
            sum1 = numbers[i]+numbers[j]
            if sum1 == target:
                return [i+1,j+1]
            elif sum1 > target:
                j -= 1
            else:
                i += 1
        return None
        
        
numbers=[2, 7, 11, 15]
target=9
Solution1 = Solution()
Solution1.twoSum(numbers, target)