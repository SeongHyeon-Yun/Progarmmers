from collections import deque

def solution(priorities, location):
    answer = 0
    process_queue = deque([(p, i) for i, p in enumerate(priorities)])  # 프로세스 큐를 생성하고 초기화합니다.

    while process_queue:
        current_process = process_queue.popleft()  # 큐에서 가장 앞에 있는 프로세스를 꺼냅니다.
        if any(current_process[0] < p[0] for p in process_queue):
            # 큐에 현재 프로세스보다 높은 우선순위의 프로세스가 있다면,
            process_queue.append(current_process)  # 현재 프로세스를 다시 큐에 넣습니다.
        else:
            answer += 1  # 현재 프로세스를 실행합니다.
            if current_process[1] == location:
                return answer  # 실행한 프로세스가 목표 프로세스인 경우, 결과를 반환하고 함수 종료합니다.
