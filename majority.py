class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        if target not in nums:
            return 0

        arr = [1 if x == target else -1 for x in nums]

        prefix = [0]
        s = 0
        for x in arr:
            s += x
            prefix.append(s)

        vals = sorted(set(prefix))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        size = len(vals)
        bit = [0] * (size + 1)

        def update(i, val):
            while i <= size:
                bit[i] += val
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0

        for p in prefix:
            idx = rank[p]
            ans += query(idx - 1)
            update(idx, 1)

        return ans