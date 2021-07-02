# 과제10. 2020 카카오 인턴십
#
# 개발자 출신으로 세계 최고의 갑부가 된 어피치는 스트레스를 받을 때면 이를 풀기 위해 오프라인 매장에 쇼핑을 하러 가곤 합니다.
# 어피치는 쇼핑을 할 때면 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있습니다.
# 어느 날 스트레스를 풀기 위해 보석 매장에 쇼핑을 하러 간 어피치는 이전처럼 진열대의 특정 범위의 보석을 모두 구매하되
# 특별히 아래 목적을 달성하고 싶었습니다.
#
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
#
# 예를 들어 아래 진열대는 4종류의 보석(RUBY, DIA, EMERALD, SAPPHIRE) 8개가 진열된 예시입니다.
# 진열대 번호 	1 	2 	3 	4 	5 	6 	7 	8
# 보석 이름 	DIA 	RUBY 	RUBY 	DIA 	DIA 	EMERALD 	SAPPHIRE 	DIA
#
# 진열대의 3번부터 7번까지 5개의 보석을 구매하면 모든 종류의 보석을 적어도 하나 이상씩 포함하게 됩니다.
#
# 진열대의 3, 4, 6, 7번의 보석만 구매하는 것은 중간에 특정 구간(5번)이 빠지게 되므로 어피치의 쇼핑 습관에 맞지 않습니다.
#
# 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다. 이때 모든 보석을 하나 이상 포함하는
# 가장 짧은 구간을 찾아서 return 하도록 solution 함수를 완성해주세요.
# 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며,
# 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.
#
#     제한사항
#         gems 배열의 크기는 1 이상 100,000 이하입니다.
#         gems 배열의 각 원소는 진열대에 나열된 보석을 나타냅니다.
#         gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있습니다.
#         gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열입니다.
#
#     입출력 예
#
# gems 	                                                                result
# ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] 	[3, 7]
# ["AA", "AB", "AC", "AA", "AC"] 	                                    [1, 3]
# ["XYZ", "XYZ", "XYZ"] 	                                            [1, 1]
# ["ZZZ", "YYY", "NNNN", "YYY", "BBB"] 	                                [1, 5]
#
#     입출력 예에 대한 설명
#
#         입출력 예 #1
#             문제 예시와 같습니다.
#
#         입출력 예 #2
#             3종류의 보석(AA, AB, AC)을 모두 포함하는 가장 짧은 구간은 [1, 3], [2, 4]가 있습니다.
#             시작 진열대 번호가 더 작은 [1, 3]을 return 해주어야 합니다.
#
#         입출력 예 #3
#             1종류의 보석(XYZ)을 포함하는 가장 짧은 구간은 [1, 1], [2, 2], [3, 3]이 있습니다.
#             시작 진열대 번호가 가장 작은 [1, 1]을 return 해주어야 합니다.
#
#         입출력 예 #4
#             4종류의 보석(ZZZ, YYY, NNNN, BBB)을 모두 포함하는 구간은 [1, 5]가 유일합니다.
#             그러므로 [1, 5]를 return 해주어야 합니다.
#
# def solution(gems):
#     return []
#
# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# print(solution(gems))
#
# gems = ["AA", "AB", "AC", "AA", "AC"]
# print(solution(gems))
#
# gems = ["XYZ", "XYZ", "XYZ"]
# print(solution(gems))
#
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# print(solution(gems))


# 문제 해설 - 이중포인터
# 맵 자료구조에서, ‘map[보석 이름] = 빈도수’로 정의를 합니다.
# 왼쪽 포인터 l과 오른쪽 포인터 r을 모두 1번 진열대에 위치시킵니다.
# 양 포인터 중, 둘 중 하나라도 진열대의 범위를 벗어나면 알고리즘을 종료합니다.
# 양 포인터가 가리키는 범위 안에 포함된 보석 종류의 개수를 세어 봅니다.(map의 사이즈를 체크합니다)
# 5-1. 범위 안에 보석 종류가 전체 보석 종류와 일치하면 더 좋은 답인지 체크한 후 l를 증가시킵니다. 그리고 2로 갑니다.
# 5-2. 범위 안에 보석 종류가 전체 보석 종류보다 작다면 r를 증가시킵니다. 그리고 3으로 갑니다.
# 즉, 왼쪽을 가리키는 포인터 l과 오른쪽을 가리키는 포인터 r을 이용하여 보석의 종류가 모자라면 r을 증가시키고,
# 보석의 종류가 충분하면 l을 증가시키는 과정을 반복하면서, 정답을 갱신시켜나갑니다.
# 이때 l을 증가시키기 이전, map자료구조에서 l번 진열대에 있던 보석의 빈도수를 감소시켜주어야 하며
# 특히 빈도수가 1에서 0이 될 때에는 map에서 완전히 제거하여야 합니다.
# r을 증가시킬 때는 map자료구조에서 증가된 r번 진열대에 있는 보석의 빈도수를 증가시켜줍니다.

def solution(gems):
    size = len(set(gems))  # 보석종류갯수
    dic = {gems[0]: 1}
    temp = [0, len(gems) - 1]  # 정답후보
    left, right = 0, 0
    while left < len(gems) and right < len(gems):
        if len(dic) == size:
            if right - left < temp[1] - temp[0]:
                temp = [left, right]
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1
        else:
            right += 1
            if right == len(gems):
                break
            if gems[right] in dic.keys():
                dic[gems[right]] += 1
            else:
                dic[gems[right]] = 1

    return [temp[0] + 1, temp[1] + 1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))

gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))