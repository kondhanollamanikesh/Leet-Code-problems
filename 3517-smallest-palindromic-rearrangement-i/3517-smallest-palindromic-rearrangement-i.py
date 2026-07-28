class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        freq = Counter(s)

        left = []
        middle = ""

        # Process characters in sorted order
        for ch in sorted(freq.keys()):
            # Add half of the occurrences to the left half
            left.append(ch * (freq[ch] // 2))

            # If frequency is odd, this is the middle character
            if freq[ch] % 2 == 1:
                middle = ch

        # Build the left half
        left = "".join(left)

        # Right half is the reverse of the left half
        right = left[::-1]

        # Construct the palindrome
        return left + middle + right