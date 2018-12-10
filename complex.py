# 허수부 j,J를 숫자 뒤에 붙힘
a=4+5j
print(a)
print(type(a))
print(isinstance(a,complex))

b=7-2J
print(a+b)

# b.real = b의 실수부, b.imag = b의 허수부
print(b.real, b.imag)

# complex(p,q) = p + qj
p = 2.5
q = -3
print(complex(p,q))

# i를 string으로 형변환
i = 10
print(type(str(i)))