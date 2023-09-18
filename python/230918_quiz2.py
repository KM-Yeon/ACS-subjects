# 연습문제 2. 학생의 수학 시험 점수를 입력 받아, 점수가 90점 이상이면 "A", 80점 이상이면 "B", 70점 이상이면
# "C", 60점 이상이면 "D", 그리고 60점 미만이면 "F"를 출력하는 프로그램을 작성하세요.

answer = int(input("수학 시험 점수를 입력하세요: "))

if answer >= 90:
    print("A")
elif answer >= 80:
    print("B")
elif answer >= 70:
    print("C")
elif answer >= 60:
    print("D")
else:
    print("F")
