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

# 대소문자와 관련된 함수
s = "i Like Python"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize()) # 문자열에서 첫번째 문자만 대문자로 바꿈
print(s.title())

# 검색 관련 객체 함수
s = "I Like Python, I Like Java Also"
f = "%s : , %d"
print("s.count('Like'): "+str(s.count("Like")))
print("s.find('Like'): "+str(s.find("Like")))           # index값 return
print(s.find("Like",5))         # 6번째부터 시작해서 Like를 찾고, Like의 첫문자의 인덱스값 return
print(s.find("JavaScript"))     # 발견하지 못하면 -1 return
print(s.rfind("Like"))          # 뒤에서부터 찾았을 때 가장 먼저 있는 문자열의 첫 문자 index값 return
print(s.index("Like"))
print(s.index("Like"))
#print(s.index("JavaScript"))       # 발견하지 못하면 예외 발생
print(s.rindex("Like"))
print(s.startswith("I Like"))
print(s.startswith("Like",2))       # Like가 index[2]에서 시작하는지
print(s.endswith("Also"))           # 전체 문자열이 Also로 끝나는지!
print(s.endswith("Java",22,26))     # 문자열, 시작index, 끝index : 끝나는 index를 맞춰줘야 true return

# 편집과 치환
s = "       spam and ham          "
print("스팸"+s.strip()+"햄")        # 앞 뒤의 공백이 없어짐
print("---"+s.rstrip()+"---")      # 뒤 공백만 없어짐
print("---"+s.lstrip()+"---")      # 앞 공백만 없어짐

s = "<><abc><><defg><><>"
print(s.strip("<>"))               # or 처리로 < 나 >를 없애줌.
print(s.strip("><"))               # 결과값 동일

s = "Hello Java"
print(s.replace("Java", "Python"))

# 정렬
s = "King and Queen"
print(s.center(60))     # 60문자 중에 s를 가운데 정렬
print(s.center(20,"-"))
print(s.ljust(20,"-"))  # 20문자 중에서 문자열은 왼쪽에 두고 오른쪽 공백을 ""안의 문자로 채움
print(s.rjust(20,"*"))  #                     오른쪽      왼쪽

# 분리와 결합
s = "Spam And Ham"
token = s.split()       # space를 기준으로 자르기
print(token[0])
print(token[1])
print(token[2])

t = s.split("And")     # And를 기준으로 자르기
print(t)

s2=":".join(t)         # 자른 t들을 :로 연결해서 문자열로 만들기
print(s2)

s3 = "one:two:three:four:five:six:seven"
print(s3.split(":"))
print(s3.split(":",2))      # 2개만 자르기
print(s3.rsplit(":",2))     # 오른쪽 2개만 자르기

lines = """1st line
2nd line
3rd line
4th line
5th line"""
print(lines.split("\n"))   # 문단을 개행으로 자르기

# 판별
print("1234".isdigit())     # 숫자인지
print("123a".isdigit())
print("abcd".isalpha())     # 문자인지
print("ab-cd".isalpha())
print("ㄱㄴㄷ".isalpha())
print("abcd".islower())     # 소문자인지
print("ABCD".isupper())     # 대문자인지
print("    ".isspace())     # 공백인지
print("".isspace())         # 아무것도 없으므로 false
print("\r\n".isspace())     # 개행은 true
print("\t".isspace())       # TAB도 true

# '0' 채우기
print("20".zfill(5))        # 20을 5자리로 만들고 왼쪽부터 0으로 채움
print("1".zfill(7))

# format str 객체 함수
f = "name:{}, age:{}"
print(f.format("둘리",10))
print("name:{}, age:{}".format("둘리",10))        # parameter의 순서를 따로 지정하지 않으면, 0부터 차례로 채워줌.
print("name:{0}, age:{1}".format("둘리",10))
print("name:{1}, age:{0}".format("둘리",10))      # parameter의 순서를 지정할 수 있음

#print("name:{name}, age:{age}".format({"age":10, "name":"둘리"}))
