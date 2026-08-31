class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            checker=target-numbers[i]
            if checker in numbers:
                j = numbers.index(checker, i + 1)
                return [i+1,j+1]
        return []