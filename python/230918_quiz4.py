# 연습문제 4. 사용자로부터 숫자를 입력 받아, 입력된 숫자들의 총합과 평균을 계산하는 프로그램을 작성하세요.
# 사용자가 0을 입력할 때까지 계속해서 숫자를 입력 받도록 합니다.

list_sum = []
range_num = 4

for _ in range(range_num):
    num = int(input("숫자를 입력하세요 (0을 입력하면 종료) : "))
    if num == 0:
        range_num -= 1
        break
    list_sum.append(num)

print(f"입력된 숫자들의 총합: {sum(list_sum)}")
print(f"입력된 숫자들의 평균: {round(sum(list_sum) / range_num, 2)}")


