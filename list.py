# 리스트 생성
l1 = []
l1 = [1, 2, "python", 4]

# indexing
print(l1[-3], l1[-2], l1[-1], l1[0], l1[1], l1[2])      # - 인덱스도 있네...

# slicing
print(l1[1:3])      # index1부터 3미만까지
print(l1[:])        # 전체!
print(l1[2:])       # index2부터 끝까지
print(l1[len(l1)-1:])   # len(l1) : 배열의 원소의 개수
print(l1[2::-1])    # index2부터 거꾸로 맨앞까지

# 반복(*)
l2 = l1 * 2
print(l2)

# 연결(+)
l3 = l1 + ["sleepy", "haaaa-am", "noooo", 4, 5, 6]
print(l3)

# 확인
print(5 in l3)

# 삭제
del l3[0]
print(l3)

# 변경 가능한 시퀀스 자료형
a = ["apple", "banana", 10, 20]
a[2] = a[2] + 90
print(a[2])


#------------------
# 슬라이싱을 통한 치환
a = [1, 12, 123, 1234]
a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20]   # a[1]을 20으로 바꿈
print(a)

a[2:3] = [30]
print(a)

# 슬라이싱을 통한 삭제
a = [1, 12, 123, 1234]

a[1:2] = []
print(a)

a[0:]=[]
print(a)

# 슬라이싱을 통한 삽입
a = [1, 12, 123, 1234]
a[1:1]

# 중간에 삽입
a[1:1] = ['a']
print(a)
a[2:2] = ['b', 'c', 'd']
print(a)

# 마지막에 삽입
a[7:] = [12345]   # 마지막 index 뒤에 슬라이싱
print(a)

# 처음에 삽입
a[0:0] = [0]
a[:0] = [9]
print(a)

#-----------------------
# list 객체함수를 통한 삽입
# 처음 삽입
a = [1, 3, 4]
a.insert(0, 9)
print(a)

# 중간 삽입
a = [1, 3, 4]
a.insert(1, 2)      # index[1] 자리에 2를 삽입
print(a)

# 끝에 삽입
a = [1, 3, 4]
a.append(5)
print(a)

# reverse
a = [1, 3, 4]
a.reverse()       # 배열의 원소들을 거꾸로 출력
print(a)

# 제거
a.remove(3)       # index가 아니라 3이라는 값이 삭제됨
print(a)

#---------------
# 스택
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
print(stack.pop())      # 마지막 항목을 뽑아서 출력하고, 그 항목을 지우기
print(stack.pop())
print(stack.pop())

#----------------
# Queue 로 사용하기
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0))        # index[0]인 항목을 뽑아서 출력하고, 그 항목을 지우기
print(q.pop(0))
print(q.pop(0))
print(q)

# sort() : list 객체 함수 : 내장된 sorting 알고리즘
l4 = [1, 5, 3, 9, 8, 4, 2]
l4.sort()           # l4 내의 항목들을 순서대로 정렬
print(l4)

l4.sort(reverse=True)   # l4 내의 항목들을 반대 순서대로 정렬
print(l4)

l5  = [19, 49, 13, 3, 68, 34, 83, 27, 58]
l5.sort(key=str)       # string으로 인식하고 sorting -> 크기 순서가 아니라 1~9까지로 정렬
print(l5)
l5.sort(key=int)       # int로 인식하고 sorting = l5.sort()와 같음!
print(l5)

# 내장 전역 함수 : sorted
l6 = [20, 10, 47, 58, 91, 64]
l7 = sorted(l6)                 # l6를 정렬한 후 새로운 리스트인 l7에 대입
print(l7)
l8 = sorted(l6, reverse = True) # l6를 크기 역순으로 정렬한 후 l8에 대입
print(l8)

def f(i):
    return i % 10

l9 = sorted(l6, key=f, reverse=False)       # f = 10으로 나눈 나머지값을 기준으로 비교
print(l9)

