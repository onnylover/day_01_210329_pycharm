#문자열을 입력 받아,
# 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
# 입력>  Python Programming!

def reverse(ss):
    for i in range(len(ss)):
        print(ss[len(ss)-i-1],end="")

s = list(input("입력> "))
reverse(s)