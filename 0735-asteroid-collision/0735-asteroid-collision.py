class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right=[]
        number=0
        n=len(asteroids)
        for i in range(n):
            if asteroids[i]>0:
                right.append(asteroids[i])
            else:
                number = -asteroids[i]

                while right and right[-1] > 0:

                    if right[-1] < number:
                        right.pop()

                    elif right[-1] == number:
                        right.pop()
                        break

                    else:
                        break

                else:
                    right.append(asteroids[i])
        return right
