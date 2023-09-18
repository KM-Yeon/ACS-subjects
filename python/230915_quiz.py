'''
학점 계산기
1. 1~100 사이의 점수를 입력받는다.
2. 점수의 범위에 따라서 각각 학점을 'A', 'B', 'C', 'D', 'F'로 출력하는 로직을 작성하세요
    A: 100이하 90초과
    B: 90이하 80초과
    C: 80이하 70초과
    D: 70이하 60초과
    F: 60이하
'''

score = int(input("점수를 입력하세요: "))

if 90 < score <= 100:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
else:
    print("F")

