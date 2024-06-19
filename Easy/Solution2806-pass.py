class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        ten = purchaseAmount // 10 * 10
        ten += 10 if purchaseAmount % 10 >= 5 else 0
        return 100 - ten
