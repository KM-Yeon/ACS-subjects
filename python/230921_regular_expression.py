import re

# 문제 1) 문자열에서 "python"이라는 단어만 찾아내는 정규표현식을 작성해보세요.
#        제시 문자열: "I love python. python is my favorite programming language"
#        결과 출력: ['python', 'python']

test1 = "I love python. python is my favorite programming language"
pattern1 = re.compile('(python)+')
result1 = pattern1.findall(test1)
print(result1)

print("=====================================================")

# 문제 2) 문자열에서 "python"이라는 단어로 시작하는 문장을 찾아내는 정규표현식을 작성해보세요.
#        제시 문자열: "python is fun. I love python."
#        결과 출력: ['python is fun.']
# '^python[a-zA-Z0-9 ]*\.$' 로 하게 되면 문장에서 .이 2개가 있기 때문에 마지막 .을 기준으로 하게 됨

test2 = "python is fun. I love python."
pattern2 = re.compile('^python[a-zA-Z0-9 ]*\.')
result2 = pattern2.findall(test2)
print(result2)

print("=====================================================")

# 문제 3) 문자열에서 "python"이라는 단어로 끝나는 문장을 찾아내는 정규표현식을 작성해보세요.
#        제시 문자열: "I love python. python is my favorite programming language. Do you
#                   like python"
#        결과 출력: ['Do you like python']

test3 = "I love python. python is my favorite programming language. Do you like python"
pattern3 = re.compile('[^\s.][a-zA-Z0-9 ]*python$')
result3 = pattern3.findall(test3)
print(result3)

print("=====================================================")

# 문제 4) 문자열에서 "python"이라는 단어가 포함된 문장을 찾아내는 정규표현식을 작성해보세요.
#        제시 문자열: "I love python. python is my favorite programming language. Do you like java"
#        결과 출력: ['I love python.', 'python is my favorite programming language.']
# ' python is ~'로 나오는데 앞에 공백 어케 지움..?

test4 = "I love python. python is my favorite programming language. Do you like java"
pattern4 = re.compile('[a-zA-Z0-9 ]*python[a-zA-Z0-9 ]*\.')
result4 = pattern4.findall(test4)
print(result4)

print("=====================================================")

# 문제 5) 문자열에서 특수문자를 찾아내는 정규표현식을 작성해보세요.
#        제시 문자열: "abc! def? ghi#"
#        결과 출력: ['!', ' ', '?', ' ', '#']

test5 = "abc! def? ghi#"
pattern5 = re.compile('[^a-zA-Z0-9]')
result5 = pattern5.findall(test5)
print(result5)

print("=====================================================")

# 문제 6) 문자열에서 공백이 아닌 특수문자를 찾아내는 정규표현식을 작성해보세요.
#        제시 문자열: "abc! def? ghi#"
#        결과 출력: ['!', '?', '#']

test6 = "abc! def? ghi#"
pattern6 = re.compile('[^a-zA-Z0-9 ]+')
result6 = pattern6.findall(test6)
print(result6)

print("=====================================================")

# 문제 7) 문자열에서 이메일 주소를 찾아내되, 사용자 이름과 도메인을 각각 분리해서 출력하는 정규표현식을 작성해보세요.
#        제시 문자열: "abc@gmail.com, def@yahoo.com, ghi@hotmail.com"
#        결과 출력: [('abc', 'gmail.com'), ('def', 'yahoo.com'), ('ghi', 'hotmail.com')]

test7 = 'abc@gmail.com, def@yahoo.com, ghi@hotmail.com'
pattern7 = re.compile('([a-zA-Z0-9]+)@([a-zA-Z0-9]+\.[a-zA-Z0-9]+)')
result7 = pattern7.findall(test7)
print(result7)

print("=====================================================")

# 문제 8) 문자열에서 HTML 태그를 찾아내되, 태그 이름만 분리해서 출력하는 정규표현식을 작성해보세요.
#      제시 문자열: '<html><body><h1>Hello, world!</h1></body></html>'
#      결과 출력: ['html', 'body', 'h1']

test8 = '<html><body><h1>Hello, world!</h1></body></html>'
pattern8 = re.compile('<(\w+)>')
result8 = pattern8.findall(test8)
print(result8)

print("=====================================================")

# 문제 9) 문자열에서 전화번호를 찾아내되, 국번과 나머지 번호를 각각 분리해서 출력하는 정규표현식을 작성해보세요.
#      제시 문자열: '010-1234-5678, 02-9876-4321, 031-8765-4321'
#      결과 출력: [('010', '1234-5678'), ('02', '9876-4321'), ('031', '8765-4321')]

test9 = '010-1234-5678, 02-9876-4321, 031-8765-4321'
pattern9 = re.compile('([0-9]{2,3})-([0-9]{4}-[0-9]{4})')
result9 = pattern9.findall(test9)
print(result9)

print("=====================================================")

# 문제 10) 문자열에서 URL을 찾아내되, 프로토콜, 도메인, 경로를 각각 분리해서 출력하는 정규표현식을 작성해보세요.
#      제시 문자열: 'https://www.google.com/search, http://www.naver.com/news, https://www.daum.net/mail'
#      결과 출력: [('https', 'www.google.com', 'search'), ('http', 'www.naver.com', 'news'), ('https', 'www.daum.net', 'mail')]

test10 = 'https://www.google.com/search, http://www.naver.com/news, https://www.daum.net/mail'
pattern10 = re.compile('(https?)://([a-zA-Z.]+)/([a-zA-Z]+)')
result10 = pattern10.findall(test10)
print(result10)

