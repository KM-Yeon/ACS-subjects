# 야구게임 만들기
# 1. 컴퓨터는 3개의 랜덤하게 뽑힌 숫자를 위치를 지정하여 입력한다. (3개의 숫자는 1 ~ 9)
#    단, 숫자 3개는 겹치지 않아야 한다.
# 2. 사용자는 랜덤한 숫자 3개를 입력해 컴퓨터가 돌린 랜덤한 숫자와 비교하여 결과를 출력한다.
# 3. 출력한 결과는 아래의 조건을 따른다.
#    * 만약 숫자가 동일하고 위치가 맞는다면 : 스트라이크
#    * 3 스트라이크일 경우 게임 종료
#    * 동일한 숫자가 있지만 위치가 다를 경우 : 볼
#    * 플레이어가 고른 숫자가 컴퓨터가 고른 숫자와 하나도 없는 경우 : 아웃
# * 플레이어는 3스트라이크가 될 때까지 게임을 진행하여 몇번만에 3스트라이크가 되었는지를 출력하면 됨
# 예) "3스트라이크 7번만에 이닝 종료"
# 예) "2S 1B 0O"


from random import *

# 3개의 숫자 랜덤하게 출력하기 (단, 겹치지 않게)
list_num = []
while True:
    rn = randint(1, 9)
    if rn not in list_num:
        list_num.append(rn)
    if len(list_num) == 3:
        break

print(list_num)
# - 숫자와 자리가 같은 경우 스트라이크 -> 문자로 변환하여 동일한지 확인
# - 숫자만 같은 경우 -> 교집합 사용, 개수가 3개여야 함
# - 하나도 없는 경우 -> else
ss = 0
bb = 0
oo = 0
while ss != 3:
    # 3개의 숫자 랜덤하게 입력 (단, 겹치지 않게)
    rand_num = list(map(int, input("3개의 숫자를 랜덤하게 입력하세요 (단 각 숫자는 1~9): ").split()))

    if (list_num[0] == rand_num[0]) or (list_num[1] == rand_num[1]) or (list_num[2] == rand_num[2]):
        ss += 1
        print("스트라이크")
    elif len(set(rand_num) & set(list_num)) >= 1:
        bb += 1
        print("ball")
    else:
        oo += 1
        print("out")

print(f"{ss}S {bb}B {oo}O")
