#입력
n, m = map(int,input().split())

# 파이썬은 수의 제한 없으니 그냥 나눗셈으로 해결
first = n//m
second = n%m

print(first)
print(second)
