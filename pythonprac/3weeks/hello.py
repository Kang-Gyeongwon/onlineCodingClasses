# print('hi')

a = 2
b = 3
print(a + b)

c = '대한'
d = '민국'
print(c + d)

# 자료형
a = ['사과', '배', '감']

print(a[0])

# 객체형
a = {'name': '영수', 'age': 24}
print(a)
print(a['name'])

# 함수
def hey():
    print('헤이')
# python 에서는 안에 실행할 코드를 tab으로 구분함 -> 반드시 지켜야 하는 룰

hey()

# 변수를 받는 함수
def sum(a, b, c):
    return a + b + c

result = sum(1, 2, 3)
print(result)

# 조건문
age = 25

if age > 20:
    print('성인입니다.')
else:
    print('청소년입니다.')

# 반복문
ages = [5, 10, 13, 23, 25, 9]

for a in ages:        # ages의 요소를 하나씩 가져와서 a로 넣고 그 a를 밑에서 사용하자
    print(a)
    if a > 20:
        print('성인입니다.')
    else:
        print('청소년입니다.')