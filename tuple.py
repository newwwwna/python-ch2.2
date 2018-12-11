    # 튜플 : 순서를 가지는 객체의 집합인 것은 list와 같지만, 수정 불가(immutable)
    # 튜플 생성
t = ()      # 공 튜플 (empty tuple)
t = (1,)    # 항목이 1개일 때는 반드시 , 를 찍어준다. 튜플인 것을 구분하기 위해서!
t = (1, 2, 3)
print(t, type(t))

    # --------------
    # sequence형 연산

# 인덱싱
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

# 슬라이싱
print(t[1:3])   # index[1] 시작, index[3] 끝 ( 끝은 포함하지 않음)
print(t[:])

#길이
print(len(t))

# tuple은 변경 불가능(immutable)한 스퀀스형이다.
t = ('apple', 'banana', 10, 20)
#t[2] = t[2] + 90   # 오류 발생 !!
print(t)

# 튜플을 이용해서 좌우변 여러개의 값을 대입(치환) 가능
x, y, z = 10, 20, 30
print(x, y, z)

# swap 도 가능
x, y = 10, 20
print(x, y)
x, y = y, x     # x, y의 값을 서로 바꾸기
print(x, y)
#

# 객체 함수 : list에 비해 많지가 않다. (immutable이기 때문에 내부값을 바꾸는 메소드들을 쓸 수 없음)
t = (20, 30, 10, 20)
print(t.index(20))      # 20이 몇번째에 있는지 index값 return
print(t.count(20))      # 20이 몇개 있는지

# 변환 : list, tuple, set
t = (2, 3, 1, 3)
print(t)

s = set(t)      # tuple을 set으로 변환 : 중복된 데이터 삭제, 항목의 값을 크기 순서대로 정렬 !
print(s)

l = list(t)     # tuple을 list로 변환
print(l)

t = tuple(l)    # list를 tuple로 변환
print(t)

# packing은 tuple로만 가능
t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking
a, b, c, s = t
print(a, b, c, s)

# 오류 : 패킹되어 있는 객체가 더 많은 경우
# a, b, c = t
# 오류 : 패킹되어 있는 객체가 더 적은 경우
# a, b, c, s, k = t

# unpacking extends
t = (1, 2, 3, 4, 5)
a, *b = t       # a에 하나만 넣고, 나머지는 b에 넣기. b가 list형으로 나옴
print(a, b)

*a, b, c = t    # b, c에 하나만 넣고, 나머지는 다 a에 넣기
print(a, b, c)

a, *b, c = t    # a, c에 하나만 넣고, 나머지는 다 b에 넣기
print(a, b, c)



