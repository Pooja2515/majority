class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1
        if n == 1:
            return m
        if n == 2:
            return (m * (m - 1)) % MOD
        size = 2 * m
        T = [[0] * size for _ in range(size)]
        for x in range(m):
            # UP,x -> DOWN,y where y < x
            for y in range(x):
                T[m + y][x] = 1
            for y in range(x + 1, m):
                T[y][m + x] = 1
        def mat_mul(A, B):
            n1 = len(A)
            n2 = len(B[0])
            mid = len(B)
            C = [[0] * n2 for _ in range(n1)]
            for i in range(n1):
                for k in range(mid):
                    if A[i][k] == 0:
                        continue
                    val = A[i][k]
                    for j in range(n2):
                        C[i][j] = (C[i][j] + val * B[k][j]) % MOD
            return C
        def mat_pow(mat, power):
            size = len(mat)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            while power:
                if power & 1:
                    result = mat_mul(result, mat)
                mat = mat_mul(mat, mat)
                power >>= 1
            return result
        V = [[0] for _ in range(size)]
        for x in range(m):
            V[x][0] = x                 
            V[m + x][0] = m - 1 - x    
        Tpow = mat_pow(T, n - 2)
        final_vec = mat_mul(Tpow, V)

        ans = 0
        for i in range(size):
            ans = (ans + final_vec[i][0]) % MOD

        return ans
