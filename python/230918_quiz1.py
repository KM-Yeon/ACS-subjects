# 연습문제 1. 사용자에게 두 개의 정수를 입력 받아, 두 정수 중에서 큰 수를 출력하는 프로그램을 작성하세요.
# 만약 두 수가 같다면, "두 수는 같습니다"라는 메시지를 출력하세요
num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

if num1 == num2:
    print("두 수는 같습니다.")
else:
    print(f"큰 수는 {max(num1, num2)}입니다.")
