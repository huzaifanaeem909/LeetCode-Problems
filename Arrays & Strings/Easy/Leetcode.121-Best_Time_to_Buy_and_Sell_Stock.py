"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""

# Solution-1:

# Time Complexity: O(n)
# Space Complexity: O(1)


def maxProfit(prices):

    min_price = float("inf")
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]

print(maxProfit(prices))

# Solution-2:

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def maxProfit(prices):

    max_profit = float('-inf')

    for i in range(len(prices)): 
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]

            if profit > 0:
                 max_profit = max(max_profit, profit)
    
    return max_profit if max_profit > float('-inf') else 0


prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]

print(maxProfit(prices))
