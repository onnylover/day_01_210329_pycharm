#숨겨진 카드의 수를 맞추는 게임입니다.
# 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
# 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게", 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다.
# 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

import random

r = random.randint(1,100)
start = 1
remark = [1,100]
print("수를 결정하였습니다. 맞추어보세요")
print("%d-%d" %(remark[0],remark[1]))
while True:
    count = "%d>>" %start
    n = int(input(count))
    if r == n :
        print("맞았습니다.")
        re = input("다시하시겠습니까 (y/n)")
        if re == "y":
            r = random.randint(1,100)
            remark = [1, 100]
            start = 1
        else:
            break
    elif r < n:
        print("더 낮게")
        start += 1
        remark[1] = n
        print("%d-%d" % (remark[0], remark[1]))
        continue
    else:
        print("더 높게")
        start += 1
        remark[0] = n
        print("%d-%d" % (remark[0], remark[1]))
        continue