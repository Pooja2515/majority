class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        max_cost = max(costs)

        # Counting sort array
        count = [0] * (max_cost + 1)

        # Count frequency of each cost
        for cost in costs:
            count[cost] += 1

        bars = 0

        # Buy from cheapest to costliest
        for cost in range(1, max_cost + 1):
            if count[cost] > 0:
                can_buy = min(count[cost], coins // cost)
                bars += can_buy
                coins -= can_buy * cost

                if coins < cost:
                    break

        return bars