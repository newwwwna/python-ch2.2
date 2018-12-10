# 문자열(str)

s = ''
str1 = 'hello world'
str2 = "hello world"
print(type(s), type(str1), type(str2))
print(isinstance(str2,str))

# 여러줄 문자열 정의
str3="""ABCDEFG
abcdef
가나다라
바사아
자차카타
파하!!!!
"""
print(str3)

# 여러줄 주석
#여러줄 문자열 사용
"""
주석1
주석2
주석3
"""

#
# 문자열 연산
str1="First String"
str2="Second String"


# 1. 인덱싱
print(str1[0], str1[2], str1[4])
print(str1[2])

# 2. 슬라이싱
#문자열 3번째 인덱스 이상, 6번째 인덱스 미만
print(str2[2:5])
#4번째 인덱스부터 끝까지
print(str2[3:])

# 3. 연결(+). + 생략 가능하다(변수일때는 안됨!!)
print(str1+str2)
print(str1+""+str2)
print("hello" "내맴~~~" "hahaha")
#

# 문자열 객체끼리 +(연결) 연산을 할 수 있다
name='홍길동'
age=40
#print(name+age) 오류 발생! string처리해주기
print(name+str(age))

# 반복(*)
print(str1*3)

# len 함수 : 문자열 길이(공백 포함)
print(len(str2))

# in, not in : true, false
print("S" in str2)
print("S" not in str2)

# 문자열 객체는 변경할 수 없다(immutable)
# str1[0]="F"

# 서식(formating) - format() 함수
print("name:"+format(name,"s")+", age:"+format(age,"d"))

# 튜플을 이용한 서식
f="name:%s, age:%d"
print(f % (name,age))
print("name:%s, age:%d" % ("둘리", 40))
#cf) C 스타일
#printf("name:%s, age:%d", name, age)

# 서식 - 딕셔너리를 이용한 formating
f = "name:%(name)s, age:%(age)d"
print(f % {"name":"둘리", "age":30})