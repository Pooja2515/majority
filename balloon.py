class Solution(object):
    def maxNumberOfBalloons(self, text):
        count = {}

        # Count characters
        for ch in text:
            count[ch] = count.get(ch, 0) + 1

        # Get required counts
        b = count.get('b', 0)
        a = count.get('a', 0)
        l = count.get('l', 0) // 2
        o = count.get('o', 0) // 2
        n = count.get('n', 0)

        return min(b, a, l, o, n)