from random import *

# up & down 문제

# 1 ~ 100 사이 숫자 랜덤으로 출력
rand_num = randint(1, 10)

# 반복
    # 입력값 필요
    # 만약 입력값이 랜덤값보다 크다면 down
    # 만약 입력값이 랜덤값보다 작다면 up
    # 같다면 정답이라는 말과 함께 return

while True:
    input_num = int(input("1 ~ 100 사이의 숫자를 입력하세요"))

    if input_num > rand_num:
        print("down")
    elif input_num < rand_num:
        print("up")
    else:
        print(f"정답입니다 : {rand_num}")
        break