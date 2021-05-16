

class RodCutting:
    def __init__(self):
        self.price = (0, 1, 5, 8, 9, 10, 14, 17, 20, 30)

    def recRodMaxPrice(self, len):
        if len == 0:
            return 0

        maxPrice = 0
        for i in range(1, len):
            leftPrice = self.price[i]
            rightPrice = self.recRodMaxPrice(len - i)
            lenPrice = leftPrice + rightPrice
            if lenPrice > maxPrice:
                maxPrice = lenPrice
        return maxPrice

if __name__=="__main__":
    rodLength = 4
    rec = RodCutting()
    maxPrice = rec.recRodMaxPrice(rodLength)
    print(maxPrice)


"""
Recurrence relationship and base condition --> memoization base condition --> DP state initialization.
"""