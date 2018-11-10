def new21Game(N, K, W):
    """
    note: the probability of i (dp[i]) is the probability of a path that ever reached i
    :type N: int, probability less than N
    :type K: int, stop when gets K or K more points
    :type W: int, draw from 1 to W
    :rtype: float
    """
    if K == 0:
        return 1
    dp = [1.0] + [0.0] * N
    Wsum = 1.0000
    for i in range(1, N + 1):
        dp[i] = Wsum / W
        if i < K:
            Wsum += dp[i]
        if 0 <= i - W < K:
            Wsum -= dp[i - W]
    print(dp)
    return sum(dp[K:])

N = 10
K = 7
W = 5
print(new21Game(N, K, W))
