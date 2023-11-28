"""You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""


def maxProfit(nums):
    left, right = 0, 1
    result = 0
    while right<len(nums):
        if nums[right]-nums[left] > 0 :
            result = max(result,nums[right]-nums[left])
        left = min(nums[left],nums[right])
        right += 1
    return result

print(maxProfit([7,6,4,3,1]))

