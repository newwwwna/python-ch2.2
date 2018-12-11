# 사전 생성 {key : value}. key는 어떤 객체가 들어와도 상관없음
d = {}          # 공사전
d = dict()      # 생성자 함수 호출
d = dict(one=1, two=2, three=3)
print(d)
d = dict([('one', 1), ('two', 2), ('three', 3)])
d = {"basketball": 5, "baseball": 9}
print(d, type(d))

# 인덱싱 대신 키로 접근해야함!
print(d["basketball"], d["baseball"])

# 연결은 지원하지 않는다(sequence형이 아님)
# print(d + {"valleyball": 6})

# 반복 지원하지 않는다(sequence형이 아님)
# print(d * 3)

# mutable(수정 가능)
d["valleyball"] = 6     # 추가
print(d)

# 다양한 key 타입
d = {}
print(d)
d[True] = 'true'
d[10] = '10'
d['twenty'] = '20'
d[(1, 2, 3)] = '6'
# 오류 : mutable 객체를 키로 사용했을 때
#l = [1, 2, 3]
#d[l] = '6'
print(d)

# keys() 함수
keys = d.keys()
print(keys, type(keys))

# for-each 구문
for key in keys:
    print(key, d[key], sep="=>")        # key => value 형식으로 print
# for(int i=0; i<=5; i++) { print(i) } 못씀..  -> for i in [0,1,2,3,4,5] : print(i)

# values() 함수
values = d.values()
for value in values:
    print(value)

# items() 함수
items = d.items()
for item in items:
    print(item)