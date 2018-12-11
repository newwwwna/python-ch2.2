    # set 생성 : 순서는 없지만, 중복 데이터는 허용하지 않음
s = {1, 2, 3}
print(s, type(s))
v = {4, 1, 7, 2, 4}
print(v)        # 중복 제거, 크기순으로 출력

    # 기본 연산
print(len(s))       # 원소가 몇 개인지
print(2 in s)       # s에 2가 있는지 : true
print(2 not in s)   # s에 2가 없는지 : false

    # list의 중복성을 제거할 때 유용
nums = [1, 2, 3, 2, 2, 4, 3, 5, 6, 6]
s = set(nums)       # nums의 중복성을 제거하고, 크기 순서대로 출력
print(s)
nums2 = list(s)     # list가 편하니까 set을 list로 변환
print(nums2)

    # 객체 함수
s.add(7)            # 7이라는 원소 추가
print(s)

s.discard(2)        # 2라는 원소를 제거
print(s)
s.discard(20)       # 에러 안남!

s.remove(3)         # 3이라는 원소를 제거
print(s)
#s.remove(10)       # 없는 원소를 제거하려고 할 때, 에러 발생

s.update({2, 3, 4}) # 중복된 데이터는 제거하고 추가시킴
print(s)

s.clear()
print(s)            # s = set() 으로 return

    # 수학 집합 관련 함수
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

# 합집합
union = s1.union(s2)
print(union)

# 교집합
inter = s1.intersection(s2)
print(inter)

# 차집합
dif = s1.difference(s2)
print(dif)

# 대칭차집합 : 합집합 - 교집합
sym_dif = s1.symmetric_difference(s2)
print(sym_dif)

# 부분집합
print(inter.issubset(s1))   # inter가 s1의 부분집합인지
print(sym_dif.issubset(s1))
print(s1.issuperset(dif))   # s1이 dif의 확대집합인지
print(union.issuperset(s2))





