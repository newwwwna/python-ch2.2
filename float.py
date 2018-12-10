
a = 1.2
print(a, type(a))
# a가 float이면 true
print(isinstance(a,float))

# 객체 함수 is_integer()는 값이 정수인지 실수인지 확인
# 타입을 확인하는 함수가 아니다. b=2.0이어도 true
b=2.00000000000
print(b,type(b))
print(b.is_integer())

# 다른 언어처럼 e, E사용한 부동소수점 표기 가능
b=2e3
c=0.2e-4
print(b,c)
#b=2000.0 c=0.00002