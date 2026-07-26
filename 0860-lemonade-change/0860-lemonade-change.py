class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        if bills[0] > 5:
            return False

        for i in bills:
            if i == 5:
                five += 1

            elif i == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1

            else:  # i == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True