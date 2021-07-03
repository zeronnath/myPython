# 최종평가
# 과제1 팰린드롬
# 문자열을 뒤에서부터 읽어도 원래 문자열과 같은 단어를 팰린드롬이라 한다.
# 입력으로 주어진 문자열이 팰린드롬인지 판별한 뒤, 팰린드롬이면 빈 문자열을 출력한다.
# 입력된 문자열이 팰린드롬이 아닐 경우 문자열을 반으로 나누어 앞부분의 단어를 기준으로 팰린드롬 단어로 만드는 함수를 작성하시오.
#
# 예시 입력1:
# 입력: s = 'abcdcba'
# 출력: ''
#
# 예시 입력2:
# 입력: s = 'bannana'
# 출력: 'bannab'
#
# 예시 입력3:
# 입력: s = 'wabe'
# 출력: 'waaw'

def solution(s):
    def is_palindrome(stra):
        return stra == stra[::-1]

    def make_palindrome(strb):
        l: int = len(strb)
        m = int(l / 2)
        half1 = strb[:m]
        return half1 + half1[::-1]

    if is_palindrome(s):
        return ''
    else:
        return make_palindrome(s)


s = 'abcdcba'
print(solution(s))
s = 'bannana'
print(solution(s))
s = 'wabe'
print(solution(s))

### final-2


### final-3


### final-4


### final-5


### final-6


### final-7


### final-8


### final-9


### final-10