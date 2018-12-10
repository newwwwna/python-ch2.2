# 2진, 8진, 10진, 16진
a = 23
print(type(a))

#2진수
b=0b1101
#8진수
o=0o23
#16진수
h=0x23
print(b,o,h)

# power = ** 로 표현. int와 long이 합쳐짐. 표현범위 무한대
e=2**1024
print(type(e))
print(e)
# 부호를 제외하고 이진수로 정수를 나타내는 데 필요한 비트 수
print(e.bit_length())

# 변환 함수
print(oct(38))
print(hex(38))