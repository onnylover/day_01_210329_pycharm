
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요.
# 1부터 99까지만 실행하세요.

i = 1
while i < 100:
    n = str(i).count("3")+str(i).count("6")+str(i).count("9")
    if n >= 1:
        print(str(i)+" "+"짝"*n)
    i += 1
