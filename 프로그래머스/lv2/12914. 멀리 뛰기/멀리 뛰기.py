def solution(n):
    # n이 2 이하인 경우, n 자체가 결과입니다.
    if n <= 2:
        return n
    
    # DP(Dynamic Programming)를 위한 리스트 생성, 초기화
    dp = [0] * (n + 1)
    dp[1] = 1  # 한 칸을 뛰는 방법은 1가지
    dp[2] = 2  # 두 칸을 뛰는 방법은 2가지

    # Bottom-up 방식의 DP를 사용하여, 작은 부분 문제부터 해결합니다.
    for i in range(3, n + 1):
        # i번째 칸까지 도달하는 방법의 수는 (i-1)번째와 (i-2)번째 칸까지 도달하는 방법의 수를 합친 것입니다.
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    
    # dp[n]은 n번째 칸까지 도달하는 방법의 수를 나타냅니다.
    return dp[n]
