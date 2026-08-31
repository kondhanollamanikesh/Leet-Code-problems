class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            checker = target - numbers[i]

            left = i + 1
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2

                if numbers[mid] == checker:
                    return [i + 1, mid + 1]

                elif numbers[mid] < checker:
                    left = mid + 1

                else:
                    right = mid - 1

        return []