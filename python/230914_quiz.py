# 연습문제 1. 다음 빈칸에 알맞은 글자를 넣어주세요
# 1
x = "Hello, World!"
y = x[7:-1]
print("{} {}".format(y, y), end=' ')
print("{}".format(y))

# 2
x = "Hello, Python!"
y = x[7:]
print("{} {}".format(y, y), end=' ')
print("{}".format(y))

# 3
x = "Learning Python is fun"
y = x[9:15]
print("{} is a part of {}".format(y, x))

# 연습문제 4. 다음 아래의 문제에서 제시하는 조건에 맞게 결과를 출력하세요.
# 1
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])

# 2
my_tuple = (10, 20, 30, 40, 50, 60, 70)
print(my_tuple[0:4])

# 3
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple[:-1])

# 4
my_tuple = (100, 200, 300, 400, 500)
print(my_tuple * 3)

# 5
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)