# 과제4. 삼성 SW 역량 테스트 유사 문제
#
# 상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
#
# 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다. 백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
#
# 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다. N = 7인 경우에 다음과 같은 상담 일정표를 보자.
#       1일 2일	3일	4일	5일	6일	7일
# Ti 	3 	5 	1 	1 	2 	4 	2
# Pi 	10 	20 	10 	20 	15 	40 	200
#
#     1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다.
#     5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.
#     상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다.
#     예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다.
#     2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.
#     또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.
#     퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
#     상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오. (힌트: 동적계획법 알고리즘을 이용하여 풀 수 있다.)
#
# 예시 입력1
#
#     입력:
#
#     N = 7
#     duration = [3, 5, 1, 1, 2, 4, 2]
#     cost = [10, 20, 10, 20, 15, 40, 200]
#
#     출력:
#
#     45
#
# 예시 입력2
#
#     입력:
#
#     N = 10
#     duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
#     cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
#
#     출력:
#
#     90
#
# 기반 코드
#
# def solution(N, duration, cost):
#     dp = [0]*(N+1)
#
#     def dynamic_programming():
#         max_val = 0
#         for i in range(N-1, -1, -1):
#            pass # 코드를 작성하여 함수를 완성하세요.
#
#         return max_val
#
#     result = dynamic_programming()
#     return result
#
#
# N = 7
# duration = [3, 5, 1, 1, 2, 4, 2]
# cost = [10, 20, 10, 20, 15, 40, 200]
# print(solution(N, duration, cost))
#
# N = 10
# duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
# cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
# print(solution(N, duration, cost))

def solution(N, duration, cost):
    dp = [0] * (N + 1)

    def dynamic_programming():
        max_val = 0
        for i in range(N - 1, -1, -1):
            time = duration[i] + i
            # 상담이 기간 내 종료하는 경우
            if time <= N:
                # 현시점까지 최고 이익 계산
                dp[i] = max(cost[i] + dp[time], max_val)
                max_val = dp[i]
            # 상담이 기간을 초과하는 경우
            else:
                dp[i] = max_val
        return max_val

    result = dynamic_programming()
    return result



N = 7
duration = [3, 5, 1, 1, 2, 4, 2]
cost = [10, 20, 10, 20, 15, 40, 200]
print(solution(N, duration, cost))

N = 10
duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
print(solution(N, duration, cost))