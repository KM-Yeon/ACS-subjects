# 응용문제 1. 문자열에서 "a"로 시작하는 단어의 개수를 계산하는 파이썬 코드를 작성하세요.
# 예를 들어, "apple ant banana acorn"이라는 문자열이 입력되면, "2"라는 결과를 출력해야 합니다.

input_words = input("문자를 입력하세요: ")

words = input_words.split()
words_list = []
for word in words:
    word = word.lower()
    if word.startswith("a"):
        words_list.append(word)

print(len(words_list))

