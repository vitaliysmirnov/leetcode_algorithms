import logging
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        logging.info('https://leetcode.com/problems/two-sum/')
        logging.debug(f'Received nums: {nums}')
        logging.debug(f'Received target: {target}')
        h = {}
        logging.info('Analyzing nums')
        for i, num in enumerate(nums):
            logging.debug(f'Index is {i}, number is {num}')
            n = target - num
            logging.debug(f'Number {n} is a match for our number {num}')
            if n not in h:
                logging.debug(f'Integer {n} has not yet been met')
                h[num] = i
                logging.debug(f'Add integer {num} with index {i} to nums collector')
            else:
                result = [h[n], i]
                logging.info(f'Found a match! {[nums[index] for index in result]}')
                return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    nums = [11, 666, 2, 7, 11, 15]
    target = 9

    Solution().twoSum(nums, target)
