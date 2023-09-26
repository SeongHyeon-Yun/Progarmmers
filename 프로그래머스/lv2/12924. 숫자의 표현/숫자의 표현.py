def solution(n):
    count = 0  # 표현 방법의 수를 저장하는 변수
    start = 1  # 시작 자연수
    end = 1    # 끝 자연수
    current_sum = 0  # 현재까지의 합
    
    while start <= n:
        if current_sum < n:
            # 현재까지의 합이 n보다 작으면 end를 증가시켜 합을 더 크게 만듭니다.
            current_sum += end
            end += 1
        elif current_sum == n:
            # 현재까지의 합이 n과 같으면 표현 방법을 찾은 것이므로 count를 증가시키고 start를 증가시켜 다음 경우를 찾습니다.
            count += 1
            current_sum -= start
            start += 1
        else:
            # 현재까지의 합이 n보다 크면 start를 증가시켜 합을 줄입니다.
            current_sum -= start
            start += 1
    
    return count