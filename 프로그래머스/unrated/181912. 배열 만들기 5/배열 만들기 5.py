def solution(intStrs, k, s, l):
    answer = []
    nums = []
    for i in range(len(intStrs)):
        nums.append(int(intStrs[i][s:s+l]))
    for j in range(len(nums)):
        if nums[j] > k:
            answer.append(nums[j])
    return answer