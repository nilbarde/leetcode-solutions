from leetcode import evaluate

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        self.early_returns = {}
        self.currentAnswer = amount + 1
        if amount %2:
            foundOdd = False
            for coin in coins:
                if coin %2:
                    foundOdd = True
                    break
            if not foundOdd:
                return -1
        coins.sort()
        result, answer = self.coinChangeSorted(coins, amount, 0)
        return answer if result else -1

    def coinChangeSorted(self, coins, amount: int, coinsUsed: int) -> int:
        if not coins:
            return False, -1
        if coinsUsed >= self.currentAnswer:
            return False, -1
        l = len(coins)
        if l in self.early_returns:
            if amount in self.early_returns[l]:
                return self.early_returns[l][amount]
        maxCoinsForLast = amount // coins[-1]
        maxCoinsForLast = min(maxCoinsForLast, self.currentAnswer - coinsUsed)
        # if amount % coins[-1] == 0:
        if maxCoinsForLast * coins[-1] == amount:
            if l not in self.early_returns: 
                self.early_returns[l] = {}
            self.early_returns[l][amount] = [True, maxCoinsForLast]
            self.currentAnswer = min(self.currentAnswer, coinsUsed + maxCoinsForLast)
            return True, maxCoinsForLast
        foundAnswer = False
        answer = amount
        for coinsForLast in range(maxCoinsForLast, -1, -1):
            val, numCoins = self.coinChangeSorted(coins[:-1], amount - coins[-1] * coinsForLast, coinsUsed + coinsForLast)
            if val:
                foundAnswer = True
                answer = min(answer, numCoins + coinsForLast)
        if foundAnswer:
            if l not in self.early_returns: 
                self.early_returns[l] = {}
            self.early_returns[l][amount] = [foundAnswer, answer]
            self.currentAnswer = min(self.currentAnswer, coinsUsed + answer)
            return foundAnswer, answer
        if l not in self.early_returns: 
            self.early_returns[l] = {}
        self.early_returns[l][amount] = [False, -1]
        return False, -1

if __name__ == "__main__":
    inputs = [
        ([1,2,5], 11),
        ([2], 3),
        ([1], 0),
        ([186,419,83,408], 6249),
        ([411,412,413,414,415,416,417,418,419,420,421,422], 9864),
        ([71,440,63,321,461,310,467,456,361], 9298),
        ([112,149,215,496,482,436,144,397,500,189], 8480),
        ([2,4,6,8,10,12,14,16,18,20,22,24], 9999),
    ]
    outputs = [
        (3),
        (-1),
        (0),
        (20),
        (24),
        (20),
        (17),
        (-1),
    ]
    x = Solution()
    evaluate(x.coinChange, inputs, outputs, evaluate_time=False)
