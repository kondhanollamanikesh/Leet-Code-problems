class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        # Count characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):

            # Try to put target[i]
            idx = ord(target[i]) - ord('a')

            if count[idx] > 0:
                ans.append(target[i])
                count[idx] -= 1

            else:
                # Cannot match target[i]
                # Find the smallest character greater than target[i]
                for j in range(idx + 1, 26):

                    if count[j] > 0:

                        ans.append(chr(j + ord('a')))
                        count[j] -= 1

                        # Put remaining characters in sorted order
                        for k in range(26):
                            ans.extend([chr(k + ord('a'))] * count[k])

                        return ''.join(ans)

                # No greater character possible.
                # Need to backtrack.
                break

        # We matched the entire target.
        # But equal is not allowed.
        # Backtrack from the right.
        while ans:

            last = ans.pop()

            count[ord(last) - ord('a')] += 1

            idx = ord(target[len(ans)]) - ord('a')

            # Find smallest character greater than target[len(ans)]
            for j in range(idx + 1, 26):

                if count[j] > 0:

                    ans.append(chr(j + ord('a')))
                    count[j] -= 1

                    # Add remaining characters in sorted order
                    for k in range(26):
                        ans.extend([chr(k + ord('a'))] * count[k])

                    return ''.join(ans)

        return ""