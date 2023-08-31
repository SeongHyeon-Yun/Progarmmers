def solution(num, total):
    # 연속된 정수의 시작값을 찾기 위해 등차수열의 합 공식 사용
    start = (2 * total - num * (num - 1)) // (2 * num)
    answer = [i for i in range(start, start + num)]
    return answer