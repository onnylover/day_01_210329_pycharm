#함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

import random

def ranTotal(r):
    rr = r
    i = 0
    total = 0
    while i < r:
         n = int(input("수를 입력하세요 (%d)번 남았습니다.: " %rr))
         total += n
         print(total)
         rr -= 1
         i += 1

r = random.randint(2,10)
ranTotal(r)
