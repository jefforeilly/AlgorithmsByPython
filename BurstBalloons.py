'''Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.append(res)
        sols = [nums]
        i = 0
        while True:
            todo = sols[i]
            if len(todo) == 1:
                res = todo[-1]
                for x in range(i, len(sols)):
                    if res < sols[x][-1]:
                        res = sols[x][-1]
                return res

            for x in range(len(todo) - 1):
                if x == 0:
                    print('--------')
                print(sols)
                if len(todo) == 2:
                    res = todo[0] + todo[-1]
                elif x == 0:
                    res = todo[x] * todo[x + 1] + todo[-1]
                elif x == len(todo) - 2:
                    res = todo[x] * todo[x - 1] + todo[-1]
                else:
                    res = todo[x] * todo[x - 1] * todo[x + 1] + todo[-1]

                sols.append(todo[:x] + todo[x + 1:-1] + [res])
            i += 1


print(Solution().maxCoins([3, 1, 5, 8]))
