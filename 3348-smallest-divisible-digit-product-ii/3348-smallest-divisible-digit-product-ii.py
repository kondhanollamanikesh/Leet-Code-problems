class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        
    

        factor = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        # --------------------------------------------------
        # Factorize t
        # --------------------------------------------------
        required = [0, 0, 0, 0]

        for i, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                required[i] += 1
                t //= p

        if t != 1:
            return "-1"

        # --------------------------------------------------
        # Convert prime-factor requirements into digits
        # --------------------------------------------------
        def get_factor_count(cnt):

            a, b, c, d = cnt

            count8, a = divmod(a, 3)
            count9, b = divmod(b, 2)

            count4, a = divmod(a, 2)
            count2 = a
            count3 = b

            count6 = 0

            # 2 * 3 -> 6
            if count2 and count3:
                count2 = 0
                count3 = 0
                count6 = 1

            # 4 * 3 -> 2 * 6
            if count4 and count3:
                count4 = 0
                count3 = 0
                count2 = 1
                count6 = 1

            return [
                0,
                0,
                count2,
                count3,
                count4,
                c,
                count6,
                d,
                count8,
                count9
            ]

        def construct(cnt):
            ans = []

            for d in range(2, 10):
                ans.append(str(d) * cnt[d])

            return ''.join(ans)

        def count_digits(cnt):
            return sum(cnt)

        # --------------------------------------------------
        # Minimum representation of t
        # --------------------------------------------------
        required_digits = get_factor_count(required)
        min_digits = count_digits(required_digits)

        n = len(num)

        # If minimum possible answer already needs more digits
        if min_digits > n:
            return construct(required_digits)

        # --------------------------------------------------
        # Count factors in num
        # --------------------------------------------------
        total = [0, 0, 0, 0]

        for ch in num:
            d = int(ch)

            for j in range(4):
                total[j] += factor[d][j]

        # --------------------------------------------------
        # If num itself works
        # --------------------------------------------------
        first_zero = num.find('0')

        if first_zero == -1:
            if all(total[j] >= required[j] for j in range(4)):
                return num

        # --------------------------------------------------
        # Scan from right to left
        # --------------------------------------------------
        prefix = total[:]

        for i in range(n - 1, -1, -1):

            d = int(num[i])

            # Remove current digit.
            # Now prefix contains factors of num[:i].
            for j in range(4):
                prefix[j] = max(
                    0,
                    prefix[j] - factor[d][j]
                )

            space = n - 1 - i

            # Cannot change a position after the first zero.
            if first_zero != -1 and i > first_zero:
                continue

            # Try a larger digit
            for bigger in range(d + 1, 10):

                remaining = []

                for j in range(4):
                    need = (
                        required[j]
                        - prefix[j]
                        - factor[bigger][j]
                    )

                    remaining.append(max(0, need))

                remaining_digits = get_factor_count(remaining)

                needed = count_digits(remaining_digits)

                if needed <= space:

                    ones = space - needed

                    suffix = (
                        '1' * ones +
                        construct(remaining_digits)
                    )

                    return (
                        num[:i] +
                        str(bigger) +
                        suffix
                    )

        # --------------------------------------------------
        # Need one extra digit
        # --------------------------------------------------
        return (
            '1' * (n + 1 - min_digits) +
            construct(required_digits)
        )