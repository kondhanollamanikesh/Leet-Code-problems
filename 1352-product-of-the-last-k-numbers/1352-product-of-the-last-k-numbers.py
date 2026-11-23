class ProductOfNumbers:

    def __init__(self):
        self.prefix=[1]

    def add(self, num: int) -> None:
        if num==0:
            self.prefix = [1]
        else:
            new_one=num*self.prefix[-1]
            self.prefix.append(new_one)

    def getProduct(self, k: int) -> int:
        if len(self.prefix)>k:
            deno=self.prefix[-k-1]
            nume=self.prefix[-1]
            return nume // deno
        return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)