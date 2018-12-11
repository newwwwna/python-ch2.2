
a = 20
b = 30
print(not a < b)
print(a < b and a != b)
print(a == b or a != b)

# True -> 1, False -> 0
print(True + 1)
print((a > b) + 1)

# bool 캐스팅( ()안에 값이 있으면 true, 없으면 false )
print(bool(10), bool(0))
print(bool(3.14), bool(0.))
print(bool('abc'), bool(''))
print(bool([1,2,3]), bool([]))
print(bool((1,2,3)), bool(()))
print(bool({1:2}), bool({}))
print(bool(None))

# 논리식의 계산 순서 : 왼쪽에서부터 계산하다가 결과값이 나오면 그 값을 return
print([] or 'logical')
print('hello' or 'world')
print('' and 'world')
print(None and 1)

s=''
s="hello world"
s or print(s)
